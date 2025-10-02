from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from typing import List

app = FastAPI()
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cuda")

class EmbedRequest(BaseModel):
    text: str

class EmbedResponse(BaseModel):
    embedding: List[float]

@app.post("/embed", response_model=EmbedResponse)
async def embed(req: EmbedRequest):
    if not req.text:
        raise HTTPException(status_code=400, detail="text is required")
    vec = model.encode(req.text)
    return {"embedding": vec.tolist() if hasattr(vec, "tolist") else list(vec)}