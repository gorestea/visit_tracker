from django.db import models


class Worker(models.Model):
    """
    Модель, представляющая работника.
    """
    name = models.CharField(max_length=255, verbose_name='Имя работника')
    phone_number = models.CharField(max_length=255, unique=True, verbose_name='Номер телефона работника')
    objects = models.Model

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


class Store(models.Model):
    """
    Модель, представляющая торговую точку.
    """
    name = models.CharField(max_length=255, verbose_name="Название торговой точки")
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE,
                               verbose_name="Работник, закрепленный за торговой точкой")
    objects = models.Model

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Торговая точка'
        verbose_name_plural = 'Торговые точки'


class Visit(models.Model):
    """
    Модель, представляющая посещение торговой точки.
    """
    datetime = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время посещения")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name="Посещаемая торговая точка")
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name="Работник, совершающий посещение")
    latitude = models.FloatField(verbose_name="Широта местоположения")
    longitude = models.FloatField(verbose_name="Долгота местоположения")
    objects = models.Model

    def __str__(self):
        return f'{self.worker.name} посетил {self.store.name} в {self.datetime}'

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'