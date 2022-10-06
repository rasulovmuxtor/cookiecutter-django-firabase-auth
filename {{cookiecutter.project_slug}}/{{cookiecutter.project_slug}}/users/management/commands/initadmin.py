from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

import os

User = get_user_model()


class Command(BaseCommand):

    def handle(self, *args, **options):
        username = os.getenv('ADMIN_USERNAME').strip()
        username_mapping = {User.USERNAME_FIELD: username}
        if not User.objects.exists(**username_mapping):
            password = os.getenv('ADMIN_PASSWORD').strip()
            user = User.objects.create_superuser(
                **username_mapping, password=password)
            user.is_active = True
            user.is_admin = True
            user.save()
            print(f'Created account with `{username}` {User.USERNAME_FIELD}')

        else:
            print(
                'Admin accounts can only be initialized if no Accounts exist')
