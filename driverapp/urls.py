from django.urls import path
from . import views

app_name = 'user'

#  ادرس های پروفایل راننده اتوبوس دار
urlpatterns = [

    path('car/create', views.CarInformationCreateView.as_view(), name='car_create_url'),

    path('car/update/<slug:slug>', views.CarInformationUpdateView.as_view(), name='car_update_url'),

    path('car/detail/<slug:slug>', views.CarDetailView.as_view(), name='car_detail_url'),

    path('property/detail/delete/<slug:slug>', views.CarDeleteView.as_view(), name='property_detail_delete_url'),

    path('comment/delete/<int:pk>/<slug:slug>', views.DeleteCommentView.as_view(), name='comment_delete'),

]