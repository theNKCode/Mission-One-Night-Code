from fastapi import FastAPI
from transformers import pipeline

## FastAPI instance
app = FastAPI()

## Text generation pipeline
pipe = pipeline("text2text-generation", model="google/flan-t5-small")

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/generate")
def generate_text(text: str):
    ## Call the text generation pipeline
    output = pipe(text)
    
    ## Return JSON response
    return {"output": output[0]['generated_text']}
