from fastapi import FastAPI

app = FastAPI(title="NLP Microservice")

@app.get("/")
def root():
    return {"message": "NLP FastAPI service is running"}
