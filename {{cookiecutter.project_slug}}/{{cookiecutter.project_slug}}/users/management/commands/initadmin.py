from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

import os

User = get_user_model()


class Command(BaseCommand):

    def handle(self, *args, **options):
        username = os.getenv('ADMIN_USERNAME').strip()
        USERNAME_FIELD = User.USERNAME_FIELD
        if not User.objects.exists(USERNAME_FIELD=username):
            password = os.getenv('password').strip()
            user = User.objects.create_superuser(
                User.USERNAME_FIELD = username, password = password)
            user.is_active = True
            user.is_admin = True
            user.save()
            print(f'Created account with `{username}` {USERNAME_FIELD}')

        else:
            print(
                'Admin accounts can only be initialized if no Accounts exist')
