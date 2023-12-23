from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

from django.db.models import Q

class AuthBackend:
    supports_object_permissions = True
    supports_anonymous_user = False
    supports_inactive_user = False

    def authenticate(self, request, email=None, password=None, **kwargs):
        User = get_user_model()

        try:
            user = get_user_model().objects.get(Q(email=email) | Q(phone=email))
        except User.DoesNotExist:
            return None

        return user if user.check_password(password) else None

    def get_user(self, user_id):
        User = get_user_model()

        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None