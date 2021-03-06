# Generated by Django 3.1.4 on 2021-02-15 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210205_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='media\\IM3.jpg', upload_to='blog_pics'),
        ),
        migrations.CreateModel(
            name='CommentsAndLikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_likes', models.IntegerField(default=0)),
                ('comment', models.CharField(max_length=200)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
            ],
        ),
    ]
