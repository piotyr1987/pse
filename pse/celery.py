import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pse.settings')

app = Celery('pse')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
