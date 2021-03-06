# Generated by Django 2.1.4 on 2018-12-14 19:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='air_conditioning',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default=None, max_length=1),
        ),
        migrations.AddField(
            model_name='product',
            name='bathrooms',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='product',
            name='bedrooms',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='product',
            name='central_eating',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default=None, max_length=1),
        ),
        migrations.AddField(
            model_name='product',
            name='city_views',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default=None, max_length=1),
        ),
        migrations.AddField(
            model_name='product',
            name='electric_range',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default=None, max_length=1),
        ),
        migrations.AddField(
            model_name='product',
            name='garage',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='product',
            name='internet',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default=None, max_length=1),
        ),
        migrations.AddField(
            model_name='product',
            name='laundry_room',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default=None, max_length=1),
        ),
        migrations.AddField(
            model_name='product',
            name='metro_central',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default=None, max_length=1),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_1',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_10',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_2',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_3',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_4',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_5',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_6',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_7',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_8',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_9',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_main',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='product',
            name='product_age',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='product',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='sqft',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='telephone',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default=None, max_length=1),
        ),
        migrations.AddField(
            model_name='product',
            name='video',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('S', 'For sale'), ('R', 'For rent')], max_length=1),
        ),
    ]
