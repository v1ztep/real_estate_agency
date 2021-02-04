# Generated by Django 2.2.4 on 2021-02-04 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20210130_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.NullBooleanField(choices=[(None, 'Не заполнено'), (True, 'Новостройка'), (False, 'Старое здание')], db_index=True, default=None, verbose_name='Новое здание'),
        ),
    ]
