import os
from celery import Celery

# Set default Django settings for 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

app = Celery('conf')

# Using a string here means the worker doesn't have to serialize 
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps
app.autodiscover_tasks()