# Generated by Django 3.0.5 on 2020-09-10 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderdata',
            name='slider_img',
            field=models.ImageField(default='', upload_to='static/css/images/'),
        ),
    ]
