from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from django.conf import settings

urlpatterns = [
    path('schema', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('ckeditor/' , include('ckeditor_uploader.urls')),
    path("admin/", admin.site.urls),
    path("account/api/" , include('account.api.urls')),
    path('property/', include('realestate.urls', namespace='property')),
    path('property/api/', include('realestate.api.urls', namespace='property_api')),
    path('driver/api/', include('driverapp.api.urls')),
    path('chef/api/', include('foodapp.api.urls', namespace='food_api')),
    path('simple_user/api/', include('simpleuser.api.urls')),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

