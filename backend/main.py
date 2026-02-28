from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

load_dotenv()


#OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")


app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI backend running"}

@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}

@app.get("/multiply")
def multiply(a: float, b: float):
    return {"result": a * b}