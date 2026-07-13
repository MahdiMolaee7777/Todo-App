from django.contrib.auth import get_user_model

User = get_user_model()


class EmailOrUsernameBackend:
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            if '@' in username:
                user = User.objects.get(email__iexact=username)
            else:
                user = User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None