# Generated by Django 2.2.4 on 2019-10-30 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=100, verbose_name='Chapter number'),
        ),
    ]