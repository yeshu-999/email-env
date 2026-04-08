from fastapi import FastAPI
from pydantic import BaseModel
from env.email_env import EmailEnv

app = FastAPI()
env = EmailEnv()

class ActionRequest(BaseModel):
    action: str

# ✅ MUST BE POST (not GET)
@app.post("/reset")
def reset():
    obs = env.reset()
    return obs

# ✅ MUST BE POST
@app.post("/step")
def step(action_req: ActionRequest):
    obs, reward, done, info = env.step(action_req.action)
    return {
        "observation": obs,
        "reward": float(reward),
        "done": bool(done),
        "info": info
    }

# ✅ MUST BE GET
@app.get("/state")
def state():
    return env.state()
