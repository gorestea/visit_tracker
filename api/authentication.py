from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import Worker
from django.core.exceptions import ObjectDoesNotExist


class PhoneAuthentication(BaseAuthentication):
    """
    Класс аутентификации по номеру телефона.
    """

    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Phone '):
            return None

        phone_number = auth_header.split(' ')[1]

        try:
            worker = Worker.objects.get(phone_number=phone_number)
        except ObjectDoesNotExist:
            raise AuthenticationFailed('Работник с указанным номером телефона не найден.')

        return (worker, None)