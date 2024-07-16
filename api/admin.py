from django.contrib import admin
from .models import Worker, Store, Visit

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    """
    Админка для модели Worker.
    """
    search_fields = ('name',)

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    """
    Админка для модели Store.
    """
    search_fields = ('name',)

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    """
    Админка для модели Visit.
    """
    search_fields = ('worker__name', 'store__name')
