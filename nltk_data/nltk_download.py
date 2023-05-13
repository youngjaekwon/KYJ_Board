import os

import nltk

FILE_DIR = os.path.dirname(os.path.abspath(__file__))

"""
nltk에 필요한 tokenizers를 다운로드
"""
nltk.download("punkt", download_dir=FILE_DIR)
