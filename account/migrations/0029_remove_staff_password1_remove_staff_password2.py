# Generated by Django 5.0.1 on 2024-03-24 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0028_rename_password_staff_password1_staff_password2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='password2',
        ),
    ]