# Generated by Django 2.1.4 on 2018-12-16 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20181215_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='photo',
            field=models.ImageField(default='download.jpg', upload_to=''),
        ),
    ]
