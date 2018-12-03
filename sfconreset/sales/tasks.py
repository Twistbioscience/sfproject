from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings
from sales.models import CustomVector, CustomVectorForContact, Contact, Account
from sfconreset.celery import app
import logging



log = logging.getLogger(__name__)


@shared_task
def repeat_query_calls():
    try:
        for x in CustomVectorForContact.objects.all():
            obj_cv = CustomVector.objects.get(id=x.vector.id)
            obj_c = Contact.objects.get(id=x.contact.id)
            obj_a = Account.objects.get(id=obj_c.account.id)
    except OSError as e:
        log.error("Stopped process, Connection error thrown {}".format(e))