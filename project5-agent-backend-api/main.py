from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent_executor

app = FastAPI()

class AgentRequest(BaseModel):
    task: str

@app.get("/")
def root():
    return {"message": "Agent backend is running"}

@app.post("/agent")
def run_agent(request: AgentRequest):
    try:
        result = agent_executor(request.task)
        return {"result": result}
    except Exception as e:
        return {
            "error": "Agent execution failed",
            "details": str(e)
        }