# Generated by Django 4.2.2 on 2023-06-24 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_alter_vets_vet_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vets',
            name='vet_name',
        ),
    ]
