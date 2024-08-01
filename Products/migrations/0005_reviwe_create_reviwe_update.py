# Generated by Django 5.0.6 on 2024-06-29 10:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_reviwe'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviwe',
            name='create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reviwe',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]