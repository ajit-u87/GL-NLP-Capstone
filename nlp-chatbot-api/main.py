from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def health_check():
    return {"message": "Welcome to NLP Chatbot API"}