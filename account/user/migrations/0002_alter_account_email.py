# Generated by Django 4.1.6 on 2023-02-16 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=254, unique=True, verbose_name='email address'),
        ),
    ]