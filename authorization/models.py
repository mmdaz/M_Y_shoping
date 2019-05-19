from django.contrib.auth.models import User


class MyUser(User):
    @classmethod
    def is_in_db(cls, user_name, password):
        user = cls.objects.filter(user_name=user_name)
        if user:
            if user.password == password:
                return True
        return False
