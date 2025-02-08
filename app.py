from fastapi import FastAPI
import faiss
import numpy as np
import json
import openai

app = FastAPI()

# Load course data
with open("courses_with_embeddings.json", "r", encoding="utf-8") as f:
    courses = json.load(f)

# Load FAISS index
index = faiss.read_index("course_embeddings.index")

api_key = "your-openai-api-key"
openai.api_key = api_key

@app.get("/search")
async def search(query: str):
    # Generate embedding for query
    response = openai.Embedding.create(input=query, model="text-embedding-ada-002")
    query_embedding = response["data"][0]["embedding"]

    # Convert to numpy array
    query_vector = np.array(query_embedding, dtype=np.float32).reshape(1, -1)

    # Search for similar courses
    _, indices = index.search(query_vector, 5)  # Top 5 results
    results = [courses[i] for i in indices[0]]

    return results
