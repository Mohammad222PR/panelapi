from django.urls import path
from . import views

app_name = 'foodapp'

#  ادرس های پروفایل ملک دار
urlpatterns = [
    path('profile/<int:pk>', views.UserFoodView.as_view(), name='user_profile_url'),

    path('profile/update/<int:pk>', views.UserFoodUpdateFormView.as_view(), name='user_profile_update_url'),

    path('food/create', views.FoodInformationUpdateView.as_view(), name='food_create_url'),

    path('food/update/<slug:slug>', views.FoodInformationUpdateView.as_view(), name='food_update_url'),

    path('food/detail/<slug:slug>', views.FoodDetailView.as_view(), name='food_detail_url'),

    path('food/detail/delete/<slug:slug>', views.FoodDeleteView.as_view(), name='food_detail_delete_url'),

    path('comment/delete/<int:pk>/<slug:slug>', views.DeleteCommentView.as_view(), name='comment_delete'),

]