import re
import os
import string
import unicodedata


def remove_punctuation(text: str) -> str:
    # remove punctuation
    return re.sub(
        r'[^\w\sàáãạảăắằẳẵặâấầẩẫậèéẹẻẽêềếểễệđìíĩỉịòóõọỏôốồổỗộơớờởỡợùúũụủưứừửữựỳỵỷỹýÀÁÃẠẢĂẮẰẲẴẶÂẤẦẨẪẬÈÉẸẺẼÊỀẾỂỄỆĐÌÍĨỈỊÒÓÕỌỎÔỐỒỔỖỘƠỚỜỞỠỢÙÚŨỤỦƯỨỪỬỮỰỲỴỶỸÝ]',
        ' ', text)


def remove_email(text: str) -> str:
    # remove email
    return re.sub(r'\S*@\S*\s?', '', text)


def remove_url(text: str) -> str:
    # remove url
    return re.sub(r'http\S+', '', text)


def remove_stopword(text: str) -> str:
    # remove stopword
    with open('vietnamese-stopwords.txt', 'r', encoding='utf8') as f:
        vn_stopwords = f.read().splitlines()
    new_text = text
    for w in vn_stopwords:
        new_text = re.sub(f'\s{w}\s', ' ', new_text)
    return new_text


def normalized(text: str) -> str:
    normalized_text = text.lower()
    normalized_text = unicodedata.normalize('NFKC', normalized_text)
    normalized_text = remove_email(normalized_text)
    normalized_text = remove_url(normalized_text)
    normalized_text = remove_punctuation(normalized_text)
    normalized_text = remove_stopword(normalized_text)
    return normalized_text
