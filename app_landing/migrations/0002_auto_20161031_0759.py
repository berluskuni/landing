# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-31 07:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_landing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, unique=True, verbose_name='Название секции')),
                ('seo_description', models.CharField(blank=True, max_length=120)),
                ('slug', models.SlugField(max_length=120)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Метки',
                'verbose_name': 'Метка',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='label',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app_landing.Label', verbose_name='Метка'),
        ),
        migrations.AddField(
            model_name='price',
            name='label',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app_landing.Label', verbose_name='Метка'),
        ),
    ]
