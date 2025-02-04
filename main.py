from fastapi import FastAPI, Body
from src.agent.agent import FashonAgent
import uvicorn

app = FastAPI()

@app.get("/generate")
async def generate(query: str = Body(..., embed=True)):
    # Assuming 'agent' is a function or class that has been defined elsewhere
    # and is responsible for generating the desired output.
    # Here, we simulate the agent's response.
    agent = FashonAgent()  # Replace with actual agent call
    chat = agent.execute_task(query)
    return {"result": chat}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8010)
