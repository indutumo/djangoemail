# Generated by Django 4.2.1 on 2023-05-12 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='group',
            new_name='status',
        ),
    ]
