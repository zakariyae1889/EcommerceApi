# Generated by Django 5.0.6 on 2024-07-06 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_alter_orderdetails_order_alter_orderdetails_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='color',
            field=models.CharField(choices=[('Read', 'Read'), ('Green', 'Green'), ('Black', 'Black'), ('White', 'White'), ('Blue', 'Blue')], default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='size',
            field=models.CharField(choices=[('s', 'S'), ('xs', 'Xs'), ('m', 'M'), ('l', 'L'), ('xl', 'Xl'), ('xxl', 'Xxl')], default='exit', max_length=255),
            preserve_default=False,
        ),
    ]