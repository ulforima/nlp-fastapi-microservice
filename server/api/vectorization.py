from fastapi import APIRouter
from server.models.corpus import TextCorpus
from server.models.vectorizers import bag_of_words, tf_idf

router = APIRouter()


@router.post("/bag-of-words")
def bow_endpoint(corpus: TextCorpus):
    return bag_of_words(corpus.texts)


@router.post("/tf-idf")
def tfidf_endpoint(corpus: TextCorpus):
    return tf_idf(corpus.texts)
