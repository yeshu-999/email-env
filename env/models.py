from pydantic import BaseModel

class Observation(BaseModel):
    email: str
    sender: str

class Action(BaseModel):
    action: str
    content: str = ""

class Reward(BaseModel):
    value: float