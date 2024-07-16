from django.db import migrations

def create_test_data(apps, schema_editor):
    Worker = apps.get_model('api', 'Worker')
    Store = apps.get_model('api', 'Store')
    Visit = apps.get_model('api', 'Visit')

    # Создание тестового работника
    worker = Worker.objects.create(name="Тестовый Работник", phone_number="123456789")

    # Создание тестовых торговых точек
    store1 = Store.objects.create(name="Тестовая Торговая Точка 1", worker=worker)
    store2 = Store.objects.create(name="Тестовая Торговая Точка 2", worker=worker)

    # Создание тестовых посещений
    Visit.objects.create(store=store1, worker=worker, latitude=55.7558, longitude=37.6176)
    Visit.objects.create(store=store2, worker=worker, latitude=59.9343, longitude=30.3351)


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(create_test_data),
    ]
