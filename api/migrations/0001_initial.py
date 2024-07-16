# Generated by Django 4.2 on 2024-07-16 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название торговой точки', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Имя работника', max_length=255)),
                ('phone_number', models.CharField(help_text='Номер телефона работника', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, help_text='Дата и время посещения')),
                ('latitude', models.FloatField(help_text='Широта местоположения')),
                ('longitude', models.FloatField(help_text='Долгота местоположения')),
                ('store', models.ForeignKey(help_text='Посещаемая торговая точка', on_delete=django.db.models.deletion.CASCADE, to='api.store')),
                ('worker', models.ForeignKey(help_text='Работник, совершающий посещение', on_delete=django.db.models.deletion.CASCADE, to='api.worker')),
            ],
        ),
        migrations.AddField(
            model_name='store',
            name='worker',
            field=models.ForeignKey(help_text='Работник, закрепленный за торговой точкой', on_delete=django.db.models.deletion.CASCADE, to='api.worker'),
        ),
    ]
