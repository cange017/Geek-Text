# Generated by Django 3.0.2 on 2020-03-09 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_payment_name_on_card'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='address',
        ),
        migrations.RemoveField(
            model_name='address',
            name='city',
        ),
        migrations.RemoveField(
            model_name='address',
            name='state',
        ),
        migrations.RemoveField(
            model_name='address',
            name='zipcode',
        ),
    ]
