# Generated by Django 5.0.3 on 2024-04-16 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_cartitem_cart_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image_field',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
