import numpy as np
import math


def tokenize_corpus(corpus):
    return [text.lower().split() for text in corpus]


def build_vocab(docs):
    vocab = []
    for doc in docs:
        for word in doc:
            if word not in vocab:
                vocab.append(word)
    return vocab


def bag_of_words(corpus):
    docs = tokenize_corpus(corpus)
    vocab = build_vocab(docs)

    bow = np.zeros((len(docs), len(vocab)), dtype=int)

    for i, doc in enumerate(docs):
        for word in doc:
            j = vocab.index(word)
            bow[i, j] += 1

    return {
        "vocab": vocab,
        "bow_matrix": bow.tolist()
    }


def tf_idf(corpus):
    docs = tokenize_corpus(corpus)
    vocab = build_vocab(docs)

    N = len(docs)
    V = len(vocab)

    tf = np.zeros((N, V))
    df = np.zeros(V)

    # TF
    for i, doc in enumerate(docs):
        doc_len = len(doc)
        if doc_len == 0:
            continue
        for word in set(doc):
            j = vocab.index(word)
            tf[i, j] = doc.count(word) / doc_len

    # DF
    for j, word in enumerate(vocab):
        df[j] = sum(1 for doc in docs if word in doc)

    # IDF
    idf = np.array([
        math.log10(N / df_j) if df_j > 0 else 0
        for df_j in df
    ])

    tfidf = tf * idf

    return {
        "vocab": vocab,
        "idf": idf.tolist(),
        "tfidf_matrix": tfidf.tolist()
    }
