from fastapi import FastAPI
from pydantic import BaseModel
import os
import openai

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

class Message(BaseModel):
    text: str

@app.post("/chat")
async def chat(msg: Message):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": msg.text}
        ]
    )

    return {
        "reply": response["choices"][0]["message"]["content"]
    }
