from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Store, Visit
from .serializers import StoreSerializer, VisitSerializer
from .authentication import PhoneAuthentication
from rest_framework.permissions import IsAuthenticated

class StoreListView(APIView):
    """
    Получение списка торговых точек, привязанных к работнику.
    """
    authentication_classes = [PhoneAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        worker = request.user
        stores = Store.objects.filter(worker=worker)

        if not stores.exists():
            return Response({'error': 'Нет торговых точек, привязанных к этому работнику'},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)


class VisitCreateView(APIView):
    """
    Создание записи о посещении торговой точки.
    """
    authentication_classes = [PhoneAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        worker = request.user
        store_id = request.data.get('store_id')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')

        try:
            store = Store.objects.get(id=store_id, worker=worker)
        except ObjectDoesNotExist:
            return Response({'error': 'Торговая точка не найдена или не привязана к работнику'},
                            status=status.HTTP_404_NOT_FOUND)

        visit = Visit.objects.create(store=store, worker=worker, latitude=latitude, longitude=longitude)
        serializer = VisitSerializer(visit)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

