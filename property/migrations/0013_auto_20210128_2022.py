# Generated by Django 2.2.4 on 2021-01-28 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20210124_0206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flat',
            old_name='owner',
            new_name='owner_deprecated',
        ),
    ]
