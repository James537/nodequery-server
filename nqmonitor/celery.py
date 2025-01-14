import os
from celery import Celery
from django.conf import settings

CELERY_RESULT_BACKEND = "mongodb"


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nqmonitor.settings")

app = Celery('EOD_TASKS',broker=settings.MONGO_BROKER_URL)

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))