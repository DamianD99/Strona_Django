# Generated by Django 3.2 on 2021-05-12 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_klijent_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cena',
            field=models.FloatField(null=True),
        ),
    ]
