# Generated by Django 5.0 on 2023-12-05 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='id',
            new_name='post_id',
        ),
    ]
