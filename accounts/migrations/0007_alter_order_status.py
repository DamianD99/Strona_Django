# Generated by Django 3.2 on 2021-05-12 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_order_cena'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pakowane', 'Pakowane'), ('W drrodze do odbioercy', 'W drrodze do odbioercy'), ('Dostarczone', 'Dostarczone')], max_length=200, null=True),
        ),
    ]
