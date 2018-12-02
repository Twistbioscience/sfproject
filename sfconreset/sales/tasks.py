from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings
from sales.models import Account
from sfconreset.celery import app


@shared_task
def repeat_query_calls():
    obj_a = Account.objects.first()
    print(obj_a.__dict__)
