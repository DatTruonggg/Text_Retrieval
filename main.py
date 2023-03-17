from doc_matrix import doc_term_matrix
import ranking


def main():
    query = "điểm thi đại học"
    rankings = ranking(query, doc_term_matrix, True)


if __name__ == '__main__':
    main()
