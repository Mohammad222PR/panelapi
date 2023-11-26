from django.urls import path , re_path
from .apiview import *

app_name = 'api_driverapp'

urlpatterns = [
    path('car/info' , UserDriverInfo.as_view() , name='driver_info'),
    path('car/user/update' , UserDriverUpdate.as_view() , name='driver_update'),
    path('car/info' , DriverCarInfoCreate.as_view() , name='driver_info'),
    path('car/info/update/<int:id>' , CarInformationUpdateView.as_view() , name='driver_info_update'),
    path('car/list' , CarListView.as_view() , name='car_list'),
    path('car/detail/<int:id>' , CarDetailView.as_view() , name='car_detail'),
    path('car/comment/create/<int:id>' , CreateCommentView.as_view() , name='car_comment_create'),
    path('car/delete/<int:id>' , DeleteCarView.as_view() , name='car_delete'),
    path('car/comment/delete/<int:id>' , DeleteCommentView.as_view() , name='car_comment_delete'),
]