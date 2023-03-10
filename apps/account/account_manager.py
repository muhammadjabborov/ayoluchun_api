from django.contrib.auth.models import BaseUserManager


class AccountManager(BaseUserManager):

    def create_user(self, username, first_name, last_name, phone, password=None):
        if not username:
            raise ValueError("Username is required")

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, phone, password):
        user = self.create_user(
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
