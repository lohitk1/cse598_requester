# Generated by Django 5.1.6 on 2025-02-05 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sorter', '0003_imagelabel_delete_selection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagelabel',
            name='user',
        ),
    ]
