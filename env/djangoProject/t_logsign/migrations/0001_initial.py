# Generated by Django 4.2.3 on 2023-08-26 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000000)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=1000000)),
                ('number', models.CharField(max_length=11)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]