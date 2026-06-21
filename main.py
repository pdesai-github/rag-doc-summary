from langchain_openai import ChatOpenAI
from flask import Flask, jsonify, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

llm =  ChatOpenAI(model="gpt-5",temperature=0)

@app.route("/ask", methods=["POST"])
def ask():   
    data = request.get_json()
    prompt = data.get("prompt")
    if not prompt:
        return jsonify({"error":"Invalid prompt"}), 400
    print(f"prompt - {prompt}")
    
    response = llm.invoke(prompt)
    
    return jsonify({
        "answer":response.content
    })

if __name__ == "__main__":
    app.run(debug=True)
