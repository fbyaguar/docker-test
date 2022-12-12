from django.urls import reverse_lazy
from django.views.generic import CreateView

from src.tasks import send_email
from src.mail.forms import MailForm
from src.mail.models import Mail


class MailView(CreateView):
    model = Mail
    form_class = MailForm
    template_name = 'mail/mail.html'
    success_url = reverse_lazy("mail:save-mail")

    def form_valid(self, form):
        form.save()
        send_email.delay(form.instance.email)
        return super().form_valid(form)
