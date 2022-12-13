import uuid

from django.contrib.auth.models import User
from django.db import models
from model_utils.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _


class Technology(models.Model):
    name = models.CharField(_('Name'), max_length=50)

    class Meta:
        verbose_name = _('Technology')
        verbose_name_plural = _('Technologies')

    def __str__(self) -> str:
        return self.name


class Profile(TimeStampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(_('First name'), max_length=50)
    last_name = models.CharField(_('Last name'), max_length=50)
    birthdate = models.DateField(_('Date of birth'))
    biography = models.TextField(_('Biography'), blank=True)
    contacts = models.EmailField(_('Email'), max_length=254, blank=False, unique=True)
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE)
    technologies = models.ManyToManyField(
        Technology,
        verbose_name=_('Technologies'),
        related_name='technologies',
    )

    def __str__(self) -> str:
        return f'Profile {self.id} | {self.first_name} {self.last_name}'

    def get_full_name(self) -> str:
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()
