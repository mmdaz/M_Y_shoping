from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def email_is_valid(email):
    try:
        validate_email(email)
        return True
    except ValidationError as e:
        return False
