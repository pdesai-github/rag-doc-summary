from pydantic import BaseModel

class PromptReq(BaseModel):
    prompt:str