# Generated by Django 4.0.6 on 2022-07-24 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authnz', '0003_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
