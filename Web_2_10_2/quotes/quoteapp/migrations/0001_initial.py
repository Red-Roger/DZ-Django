# Generated by Django 5.0.2 on 2024-02-17 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('born_date', models.CharField(max_length=150)),
                ('born_location', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('quote', models.CharField(max_length=500)),
            ],
        ),
    ]