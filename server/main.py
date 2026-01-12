from fastapi import FastAPI

app = FastAPI(title="NLP Microservice")

@app.get("/")
def root():
    return {"message": "NLP FastAPI service is running"}

from fastapi import FastAPI
from server.api.corpus import router as corpus_router

app = FastAPI(title="NLP Microservice")

app.include_router(corpus_router)

@app.get("/")
def root():
    return {"message": "NLP FastAPI service is running"}

from fastapi import FastAPI
from server.api.corpus import router as corpus_router
from server.api.vectorization import router as vector_router

app = FastAPI(title="NLP Microservice")

app.include_router(corpus_router)
app.include_router(vector_router)

@app.get("/")
def root():
    return {"message": "NLP FastAPI service is running"}

