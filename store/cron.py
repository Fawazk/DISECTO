from .models import ItemModel
import logging
logger = logging.getLogger(__name__)

def f():
    print("Cron job called")
    logger.info("Cron job called")