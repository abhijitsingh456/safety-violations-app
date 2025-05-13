from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('employees/', get_employees, name="get_employees"),
    path('vehicles/',get_vehicle_details, name="get_vehilce_details"),
    path('update_speed_violations/',update_speed_violations, name='update_speed_violations'),
    path('get_no_of_speed_violations/<str:start_date>/<str:end_date>/<int:no_of_violations>/<int:speed>/',get_no_of_speed_violations, name='get_no_of_speed_violations')
]