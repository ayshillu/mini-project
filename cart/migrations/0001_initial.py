# Generated by Django 5.0.3 on 2024-04-15 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('desc', models.CharField(max_length=100, null=True)),
                ('price', models.IntegerField(null=True)),
                ('quatity', models.IntegerField(null=True)),
            ],
        ),
    ]
