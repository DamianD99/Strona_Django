# Generated by Django 3.2 on 2021-05-12 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210512_1521'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='Klijent',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Produkty',
        ),
    ]