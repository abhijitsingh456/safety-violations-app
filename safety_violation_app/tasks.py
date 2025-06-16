from celery import shared_task
import requests
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from .models import *
from rest_framework.response import Response
import requests
from datetime import datetime, timedelta
from django.utils.timezone import make_aware
from django.db.models import Q
import logging
from django.db import IntegrityError

logger = logging.getLogger(__name__)
@shared_task
def update_safety_violations():
    logger.info("Starting Task")

    target_date = datetime.now() - timedelta(1)
    start_date = target_date.replace(hour=0,minute=0,second=0,microsecond=0)
    end_date = target_date.replace(hour=23,minute=59,second=59,microsecond=0)

    start_str = start_date.strftime('%Y-%m-%d %H:%M:%S')
    end_str = end_date.strftime('%Y-%m-%d %H:%M:%S')

    url = 'https://api.streetsoncloud.com/v4/tickets-list'
    headers = {'Content-Type': 'application/json',
                    'Range': 'items=0-10',
                    'x-api-key':'0YjoQrlmP87aseagqbw2i75weVuTONplavJn4UFu',
                    'X-Requested-With':'XMLHttpRequest'}
    final_result = []
    for i in range(-4,10):
        data = {"dateFrom":start_str,
                "dateTo":end_str,
                "exportStatus": None,
                "status":i,
                "accountId":5574,
                "units": 1,
                "optional": True}
        try:
            results = requests.post(url, json=data, headers = headers)
            results.raise_for_status()
            tickets = results.json().get('tickets',[])
            final_result.extend(tickets)
        except Exception as e:
            logger.error(F"Error fetching data from StreetsOnCloud: {e}")
            return f"Failed {str(e)}"
    logger.info(f"Fetched {len(final_result)} violations")

    for violation in final_result:
        vehicle = Vehicles.objects.filter(
        Q(first_vehicle=violation['plateText']) | Q(second_vehicle=violation['plateText'])
        ).first()
        if vehicle:
            try:
                employee = Employee.objects.get(staff_no=vehicle.staff_no)
                speed_violation = SpeedViolations(
                employee=employee,
                date=violation['dateTimeLocal'],
                location=violation['location'],
                plate_text=violation['plateText'],
                speed=int(float((violation['speedObserved'])) * 1.60934)  # mph to km/h
                )
                try:
                    speed_violation.save()
                except IntegrityError:
                    logger.info("Duplicate speed violation entry ignored.")
            except Employee.DoesNotExist:
                continue
        else:
            logger.info(f"No vehicle match found for plateText: {violation['plateText']}")
    return f"Successfully processed {len(final_result)} violations."
