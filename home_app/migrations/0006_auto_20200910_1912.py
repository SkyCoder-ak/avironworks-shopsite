# Generated by Django 3.0.5 on 2020-09-10 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0005_carddata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_head', models.CharField(default='', max_length=50)),
                ('prod_price', models.IntegerField(default=0)),
                ('prod_img', models.ImageField(default='', upload_to='images')),
            ],
        ),
        migrations.DeleteModel(
            name='CardData',
        ),
    ]
