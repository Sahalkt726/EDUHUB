# Generated by Django 5.0.1 on 2024-04-01 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_feedback_read'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='read',
        ),
    ]
