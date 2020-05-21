import pickle
import numpy as np

centers = np.loadtxt("data/centers.txt")

with open("data/variety_to_id.p", "rb") as ids:
    variety_to_id = pickle.load(ids)

id_to_variety = {id: variety for variety, id in variety_to_id.items()}


def get_varieties():
    return list(variety_to_id.keys())

def rank(positives, negatives):
    if not positives and not negatives:
        return []

    ref = np.zeros_like(centers[0])
    for p in positives:
        ref += centers[variety_to_id[p]]
    for n in negatives:
        ref -= centers[variety_to_id[n]]
    ref /= np.linalg.norm(ref)

    scores = (centers @ ref.T).ravel()
    if negatives:
        scores = (scores + 1) / 2
    ranks = np.argsort(scores)[::-1]

    return [(i, id_to_variety[r], "%.2f%%" % (100 * scores[r]) ) for i, r in enumerate(ranks)]
