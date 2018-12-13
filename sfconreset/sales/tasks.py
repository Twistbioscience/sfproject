from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings
from sales.models import CustomVector, CustomVectorForContact, Contact, Account
from sfconreset.celery import app
import logging



log = logging.getLogger(__name__)

RESULT_LIMIT = 50

@shared_task
def repeat_query_calls():
    try:
        log.info('Scriptush: Starting custom vector query')
        for custom_vector in CustomVectorForContact.objects.all()[:RESULT_LIMIT]:
            obj_cv = CustomVector.objects.get(id=custom_vector.vector.id)
            obj_c = Contact.objects.get(id=custom_vector.contact.id)
            obj_a = Account.objects.get(id=obj_c.account.id)
    except OSError as e:
        log.error('Scriptush: Stopped process, OSError was thrown {}'.format(e))