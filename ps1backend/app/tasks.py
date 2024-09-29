from time import sleep

from celery import shared_task
from celery_progress.backend import ProgressRecorder

@shared_task
def add(x, y):
    return x + y


@shared_task(bind=True)
def go_to_sleep(self, duration, amount):
    progress_recorder = ProgressRecorder(self)
    for i in range(amount):
        sleep(duration)
        progress_recorder.set_progress(i + 1, amount, f'on {i}')
    return "Done"
