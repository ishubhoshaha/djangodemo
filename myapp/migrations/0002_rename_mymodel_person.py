# Generated by Django 4.2.13 on 2024-06-02 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyModel',
            new_name='Person',
        ),
    ]