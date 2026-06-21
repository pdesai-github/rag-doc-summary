from langchain_openai import ChatOpenAI

class LLMService:
    
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-5",
            temperature=0
        )
        
    def generate_response(self, prompt:str)->str:
        res =  self.llm.invoke(prompt)
        return res.content