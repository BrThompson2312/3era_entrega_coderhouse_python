# Generated by Django 2.2.12 on 2024-05-02 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlogger', '0007_auto_20240502_1604'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogger',
            old_name='contrasenia',
            new_name='password',
        ),
    ]
