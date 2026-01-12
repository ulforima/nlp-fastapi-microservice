from pydantic import BaseModel
from typing import List

class TextCorpus(BaseModel):
    texts: List[str]
