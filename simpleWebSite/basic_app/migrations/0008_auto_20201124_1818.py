# Generated by Django 3.1.3 on 2020-11-24 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0007_auto_20201124_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='email',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='password',
        ),
    ]
