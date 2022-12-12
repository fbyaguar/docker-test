from django.urls import path

from src.mail.views import MailView

app_name = 'mail'

urlpatterns = [
    path('', MailView.as_view(), name='save-mail'),
]
