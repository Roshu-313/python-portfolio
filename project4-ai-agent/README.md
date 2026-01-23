🤖 AI Agent with Tool Use, Reasoning & Memory

A beginner-friendly yet real agentic AI system built from scratch in Python.
Demonstrates AI-based decision making, fallback logic, natural language parsing, tool usage, and short-term memory — without heavy frameworks.

📌 Project Overview

This project implements a core AI agent architecture without using LangChain, CrewAI, or other abstractions.

The agent is capable of:

Understanding user tasks written in natural language

Selecting the correct tool using AI reasoning

Falling back to rule-based logic if AI fails

Parsing human language into tool-ready inputs

Executing tools (calculator)

Remembering previous interactions (short-term memory)

This project focuses on how agents actually work internally, not just API calls.

🧠 Why This Project Matters

Most beginner AI projects stop at chatbots.

This project demonstrates agentic thinking, which is foundational for:

Autonomous AI agents

Task-oriented assistants

Recommendation engines

Multi-tool AI systems

Real-world AI products & startups

🧩 Agent Architecture

High-level flow:

User Input

Input Router

Control Commands (e.g. exit)

Memory Queries

Task Requests

AI Reasoning (Hugging Face)

Rule-Based Fallback Logic

Natural Language Parsing

Tool Execution

Memory Storage

Final Response

This separation mirrors how production-grade AI systems are designed.

🛠️ Features
✅ AI-Based Tool Selection

Uses a free Hugging Face model for reasoning

Model used: google/flan-t5-base

✅ Fallback Logic

Ensures reliability if AI fails or responds incorrectly

✅ Natural Language Parsing

Converts inputs like:

what is 100 divided by 4

Into executable expressions like:

100 / 4

✅ Tool Usage

Calculator tool using Python evaluation

Easily extensible to additional tools

✅ Short-Term Memory

Stores previous user tasks and responses

Supports queries such as:

what did i ask before

🧪 Example Usage

Input

calculate 3 + 3


Output

Result: 6


Input

what is 12 divided by 3


Output

Result: 4.0


Input

what did i ask before


Output

what is 12 divided by 3

🧰 Technologies Used

Python 3

Hugging Face Inference API (free tier)

Requests library

Custom agent architecture (no frameworks)

🚀 How to Run
1️⃣ Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2️⃣ Install dependencies
pip install requests

3️⃣ Set Hugging Face Token (Free)

Create a token on Hugging Face and set it as an environment variable.

Windows (PowerShell)

setx HF_TOKEN "your_token_here"


Linux / macOS

export HF_TOKEN="your_token_here"

4️⃣ Run the agent
python agent.py

🧠 Learning Outcomes

Through this project, I learned:

What makes an AI system an agent

How to route inputs before sending them to an AI model

Why tool input preparation is critical

How fallback logic improves reliability

How memory is handled outside the AI model

How real agentic systems are structured

🔮 Future Improvements

Add additional tools (file reading, text analysis)

Long-term memory using files or databases

Multi-step reasoning

Context-aware responses

Integration into a real application or API

👤 Author

Roshan Faisal
Computer Science Undergraduate
Aspiring AI Engineer & Agentic AI Developer

⭐ Final Note

This project is intentionally built from scratch to demonstrate understanding of agent internals rather than relying on frameworks.

Frameworks are easy to learn.
Agent thinking is the real skill.
