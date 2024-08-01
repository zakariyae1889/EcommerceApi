# Generated by Django 5.0.2 on 2024-07-29 18:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Order', '0021_remove_orderdetails_unit_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstAddress', models.CharField(max_length=255)),
                ('secondAddress', models.CharField(blank=True, max_length=255, null=True)),
                ('mobilePhone', models.CharField(max_length=255)),
                ('Country', models.CharField(max_length=255)),
                ('City', models.CharField(max_length=255)),
                ('State', models.CharField(max_length=255)),
                ('zipCode', models.PositiveIntegerField()),
                ('Payment', models.CharField(choices=[('Paypal', 'Paypal'), ('DirectCheck', 'Directcheck'), ('BankTransfer', 'Banktransfer')], max_length=255)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checkout', to='Order.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]