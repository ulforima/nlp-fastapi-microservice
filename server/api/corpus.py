from fastapi import APIRouter
from server.models.corpus import TextCorpus

router = APIRouter()

@router.post("/corpus")
def receive_corpus(corpus: TextCorpus):
    return {
        "num_texts": len(corpus.texts),
        "texts": corpus.texts
    }
