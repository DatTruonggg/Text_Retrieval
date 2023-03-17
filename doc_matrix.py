from vector import vectorize
from build_vocab import vocab, doc_lists

import tqdm

doc_term_matrix = {}
for (title, article) in tqdm(doc_lists):
    vec = vectorize(article, vocab)
    doc_term_matrix[(title, article)] = vec
