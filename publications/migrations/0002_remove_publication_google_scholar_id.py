# Generated by Django 4.2.16 on 2024-10-01 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='google_scholar_id',
        ),
    ]