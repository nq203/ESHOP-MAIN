# Generated by Django 3.1.7 on 2023-09-26 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='Name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
