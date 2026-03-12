from fastapi import FastAPI
from pydantic import BaseModel
from search import search_query

app = FastAPI()

class Query(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "AI Semantic Search API using Endee"}

@app.post("/search")
def search(query: Query):
    result = search_query(query.question)
    return {"question": query.question, "result": result}
