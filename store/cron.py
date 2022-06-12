from .models import ItemModel
from datetime import date
import logging
logger = logging.getLogger(__name__)

def update_db():
    """
    Updating the database for the expired 
    product with the help of cron job
    """
    items = ItemModel.objects.filter(is_expired=False)
    for item in items:
        if item.expiry<=date.today():
            logger.info(f"Updating item => ID: {item.id}, Name: {item.name}, Description: {item.description}")
            item.is_expired = True
            item.save()
    logger.info("Expired products updated")