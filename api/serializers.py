from rest_framework import serializers
from .models import Worker, Store, Visit


class WorkerSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Worker.
    """
    class Meta:
        model = Worker
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Store.
    """
    class Meta:
        model = Store
        fields = '__all__'


class VisitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Visit.
    """
    class Meta:
        model = Visit
        fields = '__all__'
