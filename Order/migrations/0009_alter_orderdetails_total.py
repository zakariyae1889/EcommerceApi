# Generated by Django 5.0.6 on 2024-07-24 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0008_orderdetails_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
