from django import forms

from src.mail.models import Mail


class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = '__all__'

