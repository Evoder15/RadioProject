# celeryconfig.py

BROKER_URL = 'pyamqp://guest:guest@rabbitmq:5672//'
CELERY_RESULT_BACKEND = 'mongodb://mongodb:27017/celery_results'
