# from celery import Celery
# import os

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coin_market_scrap.settings')

# # CELERY_BROKER_URL = f'amqp://{os.environ.get("RABBITMQ_DEFAULT_USER")}:{os.environ.get("RABBITMQ_DEFAULT_PASS")}@rabbit//'
# CELERY_BROKER_URL = 'amqp://localhost:5672'

# app = Celery('spinnyWorker', broker=CELERY_BROKER_URL)
# app.config_from_object('django.conf:settings', namespace='CELERY')


from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coin_market_scrap.settings')

app = Celery('coin_market_scrap')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()