# Generated by Django 3.2 on 2021-05-12 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210512_1530'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Klijent',
            new_name='Customer',
        ),
    ]
