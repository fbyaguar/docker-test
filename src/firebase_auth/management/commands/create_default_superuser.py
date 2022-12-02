from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        User.objects.create_user(username='admin',
                                 password='admin',
                                 is_staff=True,
                                 is_active=True,
                                 is_superuser=True
                                 )
        self.stdout.write('Default superuser with name=admin, pass=admin created')
