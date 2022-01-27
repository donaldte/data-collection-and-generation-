# Generated by Django 4.0.1 on 2022-01-27 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('identification', models.CharField(max_length=1000, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('Born_year', models.DateField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
