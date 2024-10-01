from time import sleep

from celery import shared_task
from celery.utils.log import get_task_logger
from celery_progress.backend import ProgressRecorder

logger = get_task_logger(__name__)


@shared_task
def add(x, y):
    return x + y


@shared_task
def sample_task():
    logger.info("The sample task just ran.")


@shared_task(bind=True)
def go_to_sleep(self, duration, amount):
    progress_recorder = ProgressRecorder(self)
    for i in range(amount):
        sleep(duration)
        progress_recorder.set_progress(i + 1, amount, f'on {i}')
    return "Done"
