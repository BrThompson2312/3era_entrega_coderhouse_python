# Generated by Django 2.2.12 on 2024-05-01 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlogger', '0003_auto_20240501_0412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogger',
            old_name='nombre',
            new_name='username',
        ),
    ]
