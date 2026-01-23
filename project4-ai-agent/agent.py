import requests
import os

agent_memory = []

def ai_decide_tool(task: str) -> str:
    """
    Uses AI to decide which tool to use.
    """
    HF_TOKEN = os.getenv("HF_TOKEN")

    if not HF_TOKEN:
        return "none"

    prompt = f"""
You are an AI agent.
Available tools:
- calculator: for math calculations

Task: {task}

Respond with ONLY one word:
calculator or none
"""

    response = requests.post(
        "https://router.huggingface.co/hf-inference/models/google/flan-t5-base",
        headers={"Authorization": f"Bearer {HF_TOKEN}"},
        json={"inputs": prompt}
    )

    result = response.json()

    try:
        decision = result[0]["generated_text"].strip().lower()
        return decision
    except:
        return "none"


def calculator(expression: str) -> str:
    """
    A simple calculator tool that evaluates math expressions.
    Example: "2 + 3 * 4"
    """
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"
    
def decide_tool(task: str) -> str:
    """
    Decides which tool to use based on the task.
    """
    math_keywords = [
    "+", "-", "*", "/",
    "calculate", "sum", "multiply",
    "divide", "divided", "minus", "plus", "times"
]


    for word in math_keywords:
        if word in task:
            return "calculator"

    return "none"
def agent_executor(task: str) -> str:
    """
    Executes the agent loop:
    Think -> Act -> Observe -> Respond
    """
    tool = ai_decide_tool(task)

    # Fallback if AI fails
    if tool == "none":
        tool = decide_tool(task)

    if tool == "calculator":
        expression = task.lower()
        expression = expression.replace("what is", "")
        expression = expression.replace("calculate", "")
        expression = expression.replace("divided by", "/")
        expression = expression.replace("divide", "/")
        expression = expression.strip()

        result = calculator(expression)

    else:
        result = "I cannot handle this task yet."

    # ✅ SAVE TO MEMORY (ALWAYS)
    agent_memory.append({
        "user": task,
        "agent": result
    })

    return result


while True:
    user_task = input("Enter your task (or 'exit'): ")

    if user_task.lower() == "exit":
        print("Agent Memory:")
        for m in agent_memory:
            print(m)
        break

    # 🧠 Memory query (handled outside agent_executor)
    if user_task.lower() == "what did i ask before":
        if agent_memory:
            print("Agent Response:", agent_memory[-1]["user"])
        else:
            print("Agent Response: I don't remember anything yet.")
        continue

    response = agent_executor(user_task)
    print("Agent Response:", response)

