import logging

from datetime import datetime

from healthnet.models import Action


console_logger = logging.getLogger(__name__)  # Used for debug output.


def log(type, description, account):
    action = Action(
        type=type,
        timePerformed=datetime.now(),
        description=description,
        account=account,
    )
    action.save()


def debug(message):
    console_logger.error(message)