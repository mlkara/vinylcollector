# Generated by Django 4.1.7 on 2023-03-01 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_listening'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listening',
            name='date',
            field=models.DateField(verbose_name='Listening Date'),
        ),
    ]