# Generated by Django 2.1.1 on 2018-09-12 03:03
from django.core.management import call_command
from django.db import migrations


def loadfixture(apps, schema_editor):
    call_command('loaddata', 'initial_data.json')


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(loadfixture)
    ]
