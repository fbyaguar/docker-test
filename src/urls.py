from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("mail/", include('src.mail.urls')),
]

api = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/customers/', include('src.customers.urls')),
]

urlpatterns += api
