from celery import shared_task
import requests

@shared_task
def update_safety_violations():
    response = requests.post('http://127.0.0.1:8000/api/update_speed_violations/')
    return response.status_code