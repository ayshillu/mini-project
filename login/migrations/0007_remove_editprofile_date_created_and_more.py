# Generated by Django 5.0.2 on 2024-04-23 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_alter_editprofile_job_alter_editprofile_profile_pic_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='editprofile',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='editprofileclient',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='editprofileclient',
            name='profile_pic',
        ),
    ]