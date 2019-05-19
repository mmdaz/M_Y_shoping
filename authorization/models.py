from django.contrib.auth.models import User


class MyUser(User):
    @classmethod
    def is_in_db(cls, user_name, password):
        user = User.objects.filter(username=user_name).first()
        if user:
            if str(user.password) == password:
                return True
        return False
