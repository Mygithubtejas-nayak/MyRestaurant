# Generated by Django 3.1.6 on 2021-03-30 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurantapp', '0002_auto_20210330_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mobile_number',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
