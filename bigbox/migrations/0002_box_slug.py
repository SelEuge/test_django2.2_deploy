# Generated by Django 2.2 on 2021-05-14 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bigbox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='slug',
            field=models.CharField(db_column='slug', default='prueba', max_length=20),
        ),
    ]
