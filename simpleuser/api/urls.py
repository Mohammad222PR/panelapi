from django.urls import path , re_path
from .apiview import *

app_name = 'simple_user_api'

urlpatterns = [
    path('simple_user/info/' , UserSimpleUserInfo.as_view() , name='simple_user_info'),
    path('simple_user/user/update' , UserSimpleUserUpdate.as_view() , name='simple_user_update'),
    path('simple_user/info/create/' , SimpleUserInformationCreateView.as_view() , name='simple_user_info_create'),
    path('simple_user/info/update/<int:id>/' , SimpleUserInformationUppdateView.as_view() , name='simple_user_info_update'),
    path('simple_user/info/list/' , SimpleUserInformationListView.as_view() , name='simple_user_info_list'),
    path('simple_user/detail/<int:id>/' , SimpleUserInformationDetailView.as_view() , name='simple_user_detail'),
    path('simple_user/delete/<int:id>/' , DeleteSimpleUserInformationView.as_view() , name='simple_user_delete'),

]