import numpy as np


def distance(a: np.ndarray, b: np.ndarray) -> np.float64:
    numerator = np.dot(a, b)
    denominator = np.linalg.norm(a) * np.linalg.norm(b)
    return numerator / denominator
