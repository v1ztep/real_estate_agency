# Generated by Django 2.2.4 on 2021-01-23 21:29

from django.db import migrations

def copy_flats_to_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(owner=flat.owner,
                                    owner_pure_phone=flat.owner_pure_phone,
                                    defaults={
                                        'owners_phonenumber': flat.owners_phonenumber,
                                    })

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20210122_2115'),
    ]

    operations = [
        migrations.RunPython(copy_flats_to_owners),
    ]
