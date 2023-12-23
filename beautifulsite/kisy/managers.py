from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email=None, phone=None, password=None, **extra_fields):
        if not password and not email:
            raise ("Дополните поля email/phone")

        if email and phone:
            email = self.normalize_email(email)

            user = self.model(
                email=email,
                phone=phone,
                **extra_fields
            )

        if extra_fields.get('is_superuser'):
            user = self.model(
                email=email,
                phone=phone,
                **extra_fields
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email=email, password=password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Не супер юзер')

        return self._create_user(
            email=email,
            password=password,
            **extra_fields
        )