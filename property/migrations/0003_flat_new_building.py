# Generated by Django 2.2.4 on 2020-12-09 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20190829_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='new_building',
            field=models.NullBooleanField(choices=[(None, 'Не заполнено'), (True, 'Новостройка'), (False, 'Старое здание')], default=None, verbose_name='Новое здание'),
        ),
    ]