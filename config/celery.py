import os
import django
<<<<<<< HEAD
<<<<<<< HEAD
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

=======
=======
>>>>>>> 4db73f897c31b5af7a61e5fc42bab3e006169e91

from celery import Celery
from django.conf import settings

from celery.schedules import crontab
<<<<<<< HEAD
>>>>>>> 3fadcee9b3fdb1e8af498ca4b836e322ffd26284
=======

>>>>>>> 4db73f897c31b5af7a61e5fc42bab3e006169e91

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

app = Celery('config')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======

>>>>>>> 4db73f897c31b5af7a61e5fc42bab3e006169e91

app.conf.beat_schedule = {
    'send_spam': {
        'task': 'config.tasks.send_spam',
        'schedule': crontab(minute='*/1'),
    },
}
<<<<<<< HEAD
>>>>>>> 3fadcee9b3fdb1e8af498ca4b836e322ffd26284
=======
>>>>>>> 4db73f897c31b5af7a61e5fc42bab3e006169e91
