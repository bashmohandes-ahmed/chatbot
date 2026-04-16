from langchain_google_genai import ChatGoogleGenerativeAI
from config import GOOGLE_API_KEY, MODEL_NAME

class AIEngine:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=MODEL_NAME, 
            google_api_key=GOOGLE_API_KEY
        )

    def get_response(self, prompt, context):
        full_query = f"Context: {context}\n\nQuestion: {prompt}"
        return self.llm.invoke(full_query).content
