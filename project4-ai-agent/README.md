# 🤖 AI Agent with Tool Use, Reasoning & Memory

> A beginner-friendly yet **real agentic AI system** built from scratch in Python, demonstrating tool usage, AI-based decision making, fallback logic, natural language parsing, and short-term memory.

---

## 📌 Project Overview

This project implements a **real AI agent architecture** without using heavy frameworks like LangChain or CrewAI.

The agent can:
- Understand user tasks
- Decide which tool to use using **AI reasoning**
- Fall back to rule-based logic if AI fails
- Parse natural language into tool-ready inputs
- Execute tools (calculator)
- Remember previous interactions (short-term memory)

This project focuses on **core agent concepts**, not just API calls.

---

## 🧠 Why This Project Matters

Most beginner AI projects are simple chatbots.  
This project demonstrates **agentic thinking**, which is the foundation of:

- Autonomous AI agents
- Task-oriented assistants
- Recommendation systems
- Multi-tool AI applications
- Future AI startups

---

## 🧩 Agent Architecture

User Input
↓
Input Router
├─ Control Commands (exit)
├─ Memory Queries
└─ Task Requests
↓
AI Reasoning (Hugging Face)
↓
Fallback Rule Logic
↓
Input Parsing Layer
↓
Tool Execution (Calculator)
↓
Memory Storage
↓
Final Response

yaml
Copy code

---

## 🛠️ Features

### ✅ AI-Based Tool Selection
- Uses a **free Hugging Face model** to decide which tool to use
- Model: `google/flan-t5-base`

### ✅ Fallback Logic
- If AI fails, a rule-based decision system ensures reliability

### ✅ Natural Language Parsing
- Converts human language like:
what is 100 divided by 4

csharp
Copy code
into:
100 / 4

markdown
Copy code

### ✅ Tool Usage
- Calculator tool using Python evaluation
- Easily extensible to more tools

### ✅ Short-Term Memory
- Stores previous user tasks and agent responses
- Enables memory queries like:
what did i ask before

yaml
Copy code

---

## 🧪 Example Usage

Enter your task (or 'exit'): calculate 3 + 3
Agent Response: Result: 6

Enter your task (or 'exit'): what is 12 divided by 3
Agent Response: Result: 4.0

Enter your task (or 'exit'): what did i ask before
Agent Response: what is 12 divided by 3

yaml
Copy code

---

## 🧰 Technologies Used

- Python 3
- Hugging Face Inference API (Free tier)
- Requests library
- Agent-based system design (no frameworks)

---

## 🚀 How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2️⃣ Install dependencies
bash
Copy code
pip install requests
3️⃣ Set Hugging Face Token (Free)
Create a token on Hugging Face and set it as an environment variable:

Windows (PowerShell):

powershell
Copy code
setx HF_TOKEN "your_token_here"
Linux / macOS:

bash
Copy code
export HF_TOKEN="your_token_here"
4️⃣ Run the agent
bash
Copy code
python agent.py
🧠 Learning Outcomes
Through this project, I learned:

What makes an AI system an agent

How to separate system commands from agent reasoning

Why tool input preparation is critical

How real agents use fallback logic

How memory is handled outside the AI model

How agentic systems are structured in production

🔮 Future Improvements
Add more tools (text analysis, file reading)

Long-term memory using files or databases

Multi-step reasoning

Context-aware responses

Integration into a real application

👤 Author
Roshan Faisal
Computer Science Undergraduate
Aspiring AI Engineer & Agentic AI Developer

⭐ Final Note
This project is intentionally built from scratch to demonstrate understanding of agent internals rather than relying on frameworks.

Frameworks can be learned quickly — agent thinking takes time.

