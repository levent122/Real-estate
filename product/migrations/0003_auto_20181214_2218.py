# Generated by Django 2.1.4 on 2018-12-14 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20181214_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sqft',
            field=models.FloatField(default=None),
        ),
    ]