# Generated by Django 4.0.1 on 2022-03-22 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title2', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=30)),
                ('currency', models.CharField(max_length=10)),
                ('sale_or_rent', models.CharField(max_length=20)),
                ('size_of_appartment', models.CharField(max_length=10)),
                ('number_or_rooms', models.CharField(max_length=10)),
                ('features', models.CharField(max_length=200)),
                ('other_features', models.CharField(max_length=200)),
                ('realtor_company_name', models.CharField(max_length=15)),
                ('date_published', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]