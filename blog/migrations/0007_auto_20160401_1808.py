# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-01 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160401_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='article/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.ImageField(upload_to='userimages/'),
        ),
    ]
