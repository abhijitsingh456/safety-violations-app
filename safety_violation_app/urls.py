from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('search_speed_violators/',search_speed_violators, name='search_speed_violators'),
    path('employees/', get_employees, name="get_employees"),
    path('vehicles/',get_vehicle_details, name="get_vehilce_details"),
    path('update_speed_violations/',update_speed_violations, name='update_speed_violations'),
    path('get_no_of_speed_violations/<str:start_date>/<str:end_date>/<int:no_of_violations>/<int:speed>/',get_no_of_speed_violations, name='get_no_of_speed_violations'),
    path('search_speed_violations/<str:staffNo>/<str:vehicleNo>/<str:start_date>/<str:end_date>/<int:speed>/',search_speed_violations, name='api for search_speed_violators'),
    path('upload_from_old_camera/',upload_from_old_camera,name="upload_from_old_camera"), #page
    path('update_from_old_camera/',update_from_old_camera,name="update_from_old_camera"), #api
    path('history_upload_from_old_camera/',history_upload_from_old_camera,name='history_upload_from_old_camera')
]