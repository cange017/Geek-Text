# Generated by Django 3.0.2 on 2020-03-09 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200309_0210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='country',
        ),
        migrations.RemoveField(
            model_name='address',
            name='county',
        ),
        migrations.RemoveField(
            model_name='address',
            name='state',
        ),
        migrations.RemoveField(
            model_name='address',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='address',
            name='city_area',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='County'),
        ),
        migrations.AddField(
            model_name='address',
            name='country_area',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='State'),
        ),
        migrations.AddField(
            model_name='address',
            name='country_code',
            field=models.CharField(blank=True, choices=[('US', 'United States of America')], max_length=100, null=True, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='address',
            name='postal_code',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Zip Code'),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Street Address'),
        ),
    ]
