# Generated by Django 3.0.2 on 2020-02-29 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('comments', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='browse.Comments')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='staticImages')),
                ('title', models.CharField(max_length=100)),
                ('rating', models.IntegerField(null=True)),
                ('genre', models.CharField(max_length=50)),
                ('topSeller', models.BooleanField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('releaseDate', models.DateTimeField()),
                ('Publisher', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='browse.Author')),
            ],
        ),
    ]
