# Generated by Django 4.0.6 on 2022-07-24 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='tag',
            field=models.ManyToManyField(related_name='interview', to='interviews.tag'),
        ),
    ]
