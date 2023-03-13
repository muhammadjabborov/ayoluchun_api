from celery import shared_task
from .utils import update_view_count


@shared_task(name='update_view_count')
def update_view_count_task(model_class, obj, user, device_id):
    print("Counter task begin")
    update_view_count(model_class, obj, user, device_id)
    print("Counter task end")
