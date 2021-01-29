# Generated by Django 2.2.4 on 2021-01-29 14:17

from django.db import migrations


def set_flat_to_owner(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        owner, created = Owner.objects.get_or_create(owner=flat.owner_deprecated,
                                    owner_pure_phone=flat.owner_pure_phone,
                                    defaults={
                                        'owners_phonenumber': flat.owners_phonenumber,
                                    })
        owner.owner_flats.set([flat])

def set_owner_to_flat(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for owner in Owner.objects.all():
        flat, created = Flat.objects.get_or_create(owner_deprecated=owner.owner,
                                    owner_pure_phone=owner.owner_pure_phone,
                                    defaults={
                                        'owners_phonenumber': owner.owners_phonenumber,
                                    })
        flat.owners.set([owner])

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20210128_2027'),
    ]

    operations = [
        migrations.RunPython(set_flat_to_owner),
        migrations.RunPython(set_owner_to_flat),
    ]
