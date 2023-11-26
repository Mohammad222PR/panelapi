from django.urls import path
from . import views

app_name = 'user'

#  ادرس های پروفایل ملک دار
urlpatterns = [
    path('profile/<int:pk>', views.UserPropertyView.as_view(), name='user_profile_url'),

    path('profile/update/<int:pk>', views.UserProperUpdateFormView.as_view(), name='user_profile_update_url'),

    path('property/create', views.PropertyInformationCreateView.as_view(), name='property_create_url'),

    path('property/update/<slug:slug>', views.PropertyInformationUpdateView.as_view(), name='property_update_url'),

    path('property/detail/<slug:slug>', views.PropertyDetailView.as_view(), name='property_detail_url'),

    path('property/detail/delete/<slug:slug>', views.PropertyDeleteView.as_view(), name='property_detail_delete_url'),

    path('comment/delete/<int:pk>/<slug:slug>', views.DeleteCommentView.as_view(), name='comment_delete'),


]