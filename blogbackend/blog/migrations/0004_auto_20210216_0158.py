# Generated by Django 3.1.4 on 2021-02-15 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210215_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='IM3.jpg', upload_to='blog_pics'),
        ),
    ]
