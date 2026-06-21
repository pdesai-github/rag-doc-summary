from langchain_openai import ChatOpenAI
from fastapi import FastAPI, HTTPException, Depends
from dotenv import load_dotenv

from models.prompt_req import PromptReq
from models.prompt_res import PromptRes
from services.llm_service import LLMService
from dependencies.services import get_llm_service

load_dotenv()

app = FastAPI()

@app.post("/chat",response_model=PromptRes)
def chat(req:PromptReq,llm_service:LLMService =  Depends(get_llm_service)):      
    prompt = req.prompt
    if not prompt:
        raise HTTPException(
            status_code=400,
            detail="Invalid prompt"
        )
    print(f"prompt - {prompt}")

    response = llm_service.generate_response(prompt)
    
    return PromptRes(
        response=response
    )
