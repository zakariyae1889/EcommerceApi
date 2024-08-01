# Generated by Django 5.0.2 on 2024-07-28 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0014_order_total_amount_orderdetails_unit_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetails',
            old_name='unit_price',
            new_name='price_unit',
        ),
        migrations.AlterField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]