# Generated by Django 2.2.4 on 2019-10-30 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191030_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='amt_raised',
        ),
        migrations.RemoveField(
            model_name='post',
            name='amt_sought',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_status',
        ),
    ]