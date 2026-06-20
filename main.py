from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

def main():
    llm =  ChatOpenAI(model="gpt-5",temperature=0)
    response = llm.invoke("What is Spec driven development?")
    print(response.content)


if __name__ == "__main__":
    main()
