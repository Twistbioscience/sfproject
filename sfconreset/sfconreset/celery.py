from __future__ import absolute_import, unicode_literals

import os
import logging
import traceback as tb

from celery import Celery
from celery.signals import before_task_publish, task_failure
# from django.conf import settings
#
# settings.configure()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sfconreset.settings')

app = Celery('sfconreset')
app.conf.broker_url = os.getenv('BROKER_URL', 'redis://localhost/')
app.conf.result_backend = os.getenv('RESULT_BACKEND', 'redis://localhost/')
app.conf.beat_schedule = {
    'poll every %s seconds ' % str(1): {
        'task': 'sales.tasks.repeat_query_calls',
        'schedule': float(1),
        'args': (),
    },
}
app.conf.accept_content = ['application/json']
app.conf.task_serializer = 'json'
app.conf.task_default_queue = 'celery'

logger = logging.getLogger('sfconreset')


# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@task_failure.connect
def task_failure_handler(task_id="", exception=None, traceback=None, **kwargs):
    msg_tpl = 'Task {} failed with exception {}. Traceback: {}'
    formatted_tb = '\n'.join(tb.format_tb(traceback)) if traceback else 'no tb'

    client.captureMessage(
        "Unhandled error in celery task",
        data={"exception": str(exception), "traceback": formatted_tb},
        tags={"from": "celery-global-catcher"}
    )


    msg = msg_tpl.format(task_id, str(exception), formatted_tb)

    logger.error(msg)
