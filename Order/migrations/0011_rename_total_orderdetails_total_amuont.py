# Generated by Django 5.0.6 on 2024-07-24 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0010_alter_orderdetails_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetails',
            old_name='total',
            new_name='total_amuont',
        ),
    ]
