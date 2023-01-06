import os
import django
<<<<<<< HEAD
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

=======

from celery import Celery
from django.conf import settings

from celery.schedules import crontab
>>>>>>> 3fadcee9b3fdb1e8af498ca4b836e322ffd26284

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

app = Celery('config')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
<<<<<<< HEAD
=======

app.conf.beat_schedule = {
    'send_spam': {
        'task': 'config.tasks.send_spam',
        'schedule': crontab(minute='*/1'),
    },
}
>>>>>>> 3fadcee9b3fdb1e8af498ca4b836e322ffd26284
