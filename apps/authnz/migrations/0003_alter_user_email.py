# Generated by Django 4.0.6 on 2022-07-24 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authnz', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=250),
        ),
    ]
