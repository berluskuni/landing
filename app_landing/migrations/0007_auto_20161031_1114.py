# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-31 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_landing', '0006_post_icons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_post',
            field=models.ManyToManyField(blank=True, related_name='image_post', to='app_landing.Images'),
        ),
    ]