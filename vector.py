import Preprocess
from Preprocess import normalized
import numpy as np


def vectorize(text: str, vocab: list) -> np.ndarray:
    normalized_text = Preprocess.normalized(text)
    vec = []
    for word in vocab:
        if word in normalized_text:
            vec.append(1)
        else:
            vec.append(0)

    return np.array(vec)
