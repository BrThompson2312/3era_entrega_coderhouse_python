# Generated by Django 2.2.12 on 2024-05-01 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlogger', '0004_auto_20240501_0415'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='blogImages')),
                ('blog', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AppBlogger.Blog')),
            ],
        ),
    ]
