from vector import vectorize
from distance import distance
from build_vocab import vocab


def ranking(query: str, doc_term_matrix: dict, print_top_10: bool = True) -> list:
    query_vec = vectorize(query, vocab)
    rankings = []
    i = 1
    for doc_info, vec in doc_term_matrix.items():
        score = distance(query_vec, vec)
        rankings.append((score, (doc_info[0])))
        i += 1
    rankings.sort(reverse=True)

    if print_top_10 == True:
        for rank in rankings[:10]:
            print(rank)

    return rankings
