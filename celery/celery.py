# celery.py

from celery import Celery
from celeryconfig import BROKER_URL, CELERY_RESULT_BACKEND

app = Celery('celery', broker=BROKER_URL, backend=CELERY_RESULT_BACKEND)

# Include tasks from all modules in the tasks package
app.autodiscover_tasks(['tasks'])
