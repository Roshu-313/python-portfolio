# 🤖 Agent Backend API (Project 5)

A production-style **agentic AI backend service** built with FastAPI.  
This project exposes an intelligent, tool-using agent as a **reliable JSON API**, following real-world backend architecture principles.

---

## 📌 Project Purpose

The goal of this project is to convert a locally running AI agent into a **backend service** that:

- Can be consumed by any frontend or external system
- Accepts structured JSON input
- Returns structured JSON output
- Remains stable even when the agent fails

This mirrors how modern AI systems (ChatGPT, Gemini, Claude, Copilot) are deployed in production.

---

## 🧠 What This Agent Can Do

- Accept natural language tasks via an API
- Decide whether to use tools (AI-based + rule-based fallback)
- Perform math calculations using a calculator tool
- Maintain short-term memory of interactions
- Safely handle errors without crashing the server

---

## 🏗️ Architecture Overview

Client (Browser / App / API)
↓
FastAPI (API Layer)
↓
Agent Executor
↓
Tool Selection (AI + Rules)
↓
Tool Execution (Calculator)


Key design principle:
> **Agents can fail, APIs must not.**

---

## 🧩 Key Concepts Used

- Agent executor pattern
- Tool selection (AI + fallback rules)
- Separation of concerns (API vs agent logic)
- Safe execution boundaries
- JSON request/response contracts
- Memory storage (in-process)

---

## 📁 Project Structure

agent-backend-api/
│
├── main.py # FastAPI app (API layer)
├── agent.py # Agent logic (reasoning, tools, memory)
├── requirements.txt # Project dependencies
└── README.md


---

## ⚙️ Technologies Used

- Python 3
- FastAPI
- Uvicorn
- Hugging Face Inference API
- Requests
- Pydantic

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

```bash
python -m pip install -r requirements.txt
2️⃣ Set Hugging Face Token (Optional but Recommended)
Create a free token at: https://huggingface.co/settings/tokens

Then set it as an environment variable:

Windows (PowerShell):

setx HF_TOKEN "your_token_here"
macOS / Linux:

export HF_TOKEN="your_token_here"
3️⃣ Start the API Server
python -m uvicorn main:app --reload
4️⃣ Test the API
Open your browser at:

http://127.0.0.1:8000/docs
Use the POST /agent endpoint with JSON input:

{
  "task": "what is 100 divided by 4"
}
Example response:

{
  "result": "Result: 25"
}
🧪 CLI Mode (Optional)
The agent can also be run directly in the terminal:

python agent.py
This is useful for local testing and debugging.

🛡️ Reliability & Safety
Agent errors do not crash the API

All failures return controlled JSON responses

Clear separation between:

API layer

Agent logic

Tool execution

This makes the system deployable and extensible.

🚀 What’s Next
This project is part of a larger roadmap toward advanced agentic AI systems.

Upcoming projects include:

RAG-based agents (document knowledge)

Multi-tool intelligent agents

Multi-agent coordination

Full-stack agentic AI systems

Product-level AI applications

👤 Author
Roshan Faisal
BSCS Student | Agentic AI & Generative AI Developer
Focused on building real-world AI systems, not demos.
