import Preprocess
from Preprocess import normalized
import os
import unicodedata
#lấy dữ liệu từ bước tiền xử lý
folder_path = "D://DatTruong//All//2025//Mini_project//news_corpus"  # đường dẫn đến thư mục chứa các tệp tin
vocab = []
doc_lists =[]
filenames = os.listdir(folder_path)

for i in range(len(filenames)):
    filename = filenames[i]
    filepath = os.path.join(folder_path, filename)

    with open(filepath, 'r', encoding='utf8') as f:
        lines = list(filter(None, f.read().splitlines()))
        title = unicodedata.normalize('NFKC', lines[0].strip())
        article = ' '.join(lines[1:]).strip()
        article = Preprocess.normalized(article)
        if article == '':
            continue
        else:
            if (title, article) not in doc_lists:
                doc_lists.append((title, article))
            tokens = list(filter(None, article.split(' ')))
            for token in tokens:
                if token not in vocab:
                    vocab.append(token)