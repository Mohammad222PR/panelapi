from django.urls import path , re_path
from .apiview import *

app_name = 'realestate_api'

urlpatterns = [
    path('realestate/info/' , UserRealeStateInfo.as_view() , name='realestate_info'),
    path('realestate/user/update' , UserRealeStateUpdate.as_view() , name='realestate_update'),
    path('realestate/property/info/create/' , PropertyInformationCreateView.as_view() , name='realestate_property_info_create'),
    path('realestate/property/info/update/<int:id>/' , PropertyInformationUppdateView.as_view() , name='realestate_property_info_update'),
    path('realestate/property/info/list/' , PropertyInformationListView.as_view() , name='realestate_property_info_list'),
    path('realestate/property/detail/<int:id>/' , PropertyInformationsDetailView.as_view() , name='realestate_property_info_detail'),
    path('realestate/comment/create/<int:id>/' , CreateCommentView.as_view() , name='realestate_comment_create'),
    path('realestate/delete/<int:id>/' , DeletePropertyInformationView.as_view() , name='realestate_delete'),
    path('realestate/comment/delete/<int:id>/' , DeleteCommentView.as_view() , name='realestate_comment_delete'),
]