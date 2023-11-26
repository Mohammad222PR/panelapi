from django.urls import path , re_path
from .apiview import *

app_name = 'foodapp_api'

urlpatterns = [
    path('chef/info' , UserChefInfo.as_view() , name='chef_info'),
    path('chef/user/update' , UserChefUpdate.as_view() , name='chef_update'),
    path('chef/food/info' , ChefInformationCreateView.as_view() , name='chef_food_info'),
    path('chef/food/info/update/<int:id>' , ChefInformationUppdateView.as_view() , name='chef_food_info_update'),
    path('chef/food/info/list/' , ChefInformationListView.as_view() , name='chef_food_info_list'),
    path('chef/info/detail/<int:id>' , ChefInformationsDetailView.as_view() , name='chef_info_detail'),
    path('chef/comment/create/<int:id>' , CreateCommentView.as_view() , name='chef_comment_create'),
    path('chef/delete/<int:id>' , DeleteChefInformationView.as_view() , name='chef_delete'),
    path('chef/comment/delete/<int:id>' , DeleteCommentView.as_view() , name='chef_comment_delete'),
]