from langchain_openai import ChatOpenAI
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

from models.prompt_req import PromptReq
from models.prompt_res import PromptRes

load_dotenv()

app = FastAPI()

llm =  ChatOpenAI(model="gpt-5",temperature=0)

@app.post("/chat",response_model=PromptRes)
def chat(req:PromptReq):      
    prompt = req.prompt
    if not prompt:
        raise HTTPException(
            status_code=400,
            detail="Invalid prompt"
        )
    print(f"prompt - {prompt}")

    response = llm.invoke(prompt)
    
    return PromptRes(
        response=response.content
    )
