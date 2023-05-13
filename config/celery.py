from __future__ import absolute_import, unicode_literals

import os
from datetime import timedelta

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    # Post의 토큰 및 연관게시글을 업데이트하는 schedule
    "update_posts_every_five_minutes": {
        "task": "board.tasks.update_post_task",
        # 매 5분마다 실행
        "schedule": timedelta(minutes=5),
        # 실행 요청 후 2분이 지나도 실행이 안되면 expire
        "options": {"expires": 2 * 60},  # 2minute
    }
}
