from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("mail/", include('src.mail.urls')),
]

api = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/customers/', include('src.customers.urls')),
    re_path(r'^api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

urlpatterns += api
