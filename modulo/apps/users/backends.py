# debes importar tu modelo de usuario, independiente de cual sea
from .models import User

class UserAuth(object):
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(username=username)
            print("Backend")
            print(user.username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user =  User.objects.get(Licence=user_id)
            if user.is_active:
                return user
            return None

        except User.DoesNotExist:
            return None
