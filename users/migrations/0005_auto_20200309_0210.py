# Generated by Django 3.0.2 on 2020-03-09 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200309_0202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='city_area',
            new_name='county',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='country_area',
            new_name='state',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='postal_code',
            new_name='zip_code',
        ),
        migrations.RemoveField(
            model_name='address',
            name='country_code',
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.CharField(blank=True, choices=[('US', 'United States of America')], max_length=100, null=True),
        ),
    ]
