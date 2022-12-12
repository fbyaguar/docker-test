from src.mail.models import Mail
from src.celeryapp import app
from django.core.mail import send_mail


@app.task
def send_email(mail):
    send_mail(
        'Тестим отправку писем',
        'Поздравляем. Вы получили наше письмо',
        'fbyaguar@gmail.com',
        [mail],
        fail_silently=False,
    )


@app.task
def send_periodic_email():
    for mail in Mail.objects.all():
        send_mail(
            'Тестим отправку писем',
            'Поздравляем. Вы получили наше письмо',
            'fbyaguar@gmail.com',
            [mail.email],
            fail_silently=False,
        )
