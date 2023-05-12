import os

import nltk

from django.conf import settings

"""
nltk의 기본 디렉토리 설정
"""
nltk.data.path.append(os.path.join(settings.BASE_DIR, "nltk_data"))
