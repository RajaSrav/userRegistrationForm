# Generated by Django 2.2.7 on 2020-05-01 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0003_auto_20200501_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
