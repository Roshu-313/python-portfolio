import requests
import os

# -------------------------
# Agent Memory
# -------------------------
agent_memory = []

# -------------------------
# AI Tool Decider (Hugging Face)
# -------------------------
def ai_decide_tool(task: str) -> str:
    HF_TOKEN = os.getenv("HF_TOKEN")

    if not HF_TOKEN:
        return "none"

    prompt = f"""
You are an AI agent.

Available tools:
- calculator (for math calculations)

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
    except Exception:
        return "none"


# -------------------------
# Calculator Tool
# -------------------------
def calculator(expression: str) -> str:
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"


# -------------------------
# Rule-Based Tool Decider (Fallback)
# -------------------------
def decide_tool(task: str) -> str:
    math_keywords = [
        "+", "-", "*", "/",
        "calculate", "sum", "multiply",
        "divide", "divided", "minus", "plus", "times"
    ]

    for word in math_keywords:
        if word in task.lower():
            return "calculator"

    return "none"


# -------------------------
# Agent Executor (CORE)
# -------------------------
def agent_executor(task: str) -> str:
    # 1. Decide tool (AI first)
    tool = ai_decide_tool(task)

    # 2. Fallback to rules
    if tool == "none":
        tool = decide_tool(task)

    # 3. Act
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

    # 4. Save to memory
    agent_memory.append({
        "user": task,
        "agent": result
    })

    return result


# -------------------------
# CLI Runner (ONLY for terminal use)
# -------------------------
if __name__ == "__main__":
    while True:
        task = input("Enter your task (or 'exit'): ")
        if task.lower() == "exit":
            break
        print(agent_executor(task))