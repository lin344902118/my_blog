# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-29 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u59d3\u540d')),
                ('email', models.EmailField(max_length=50, verbose_name='\u90ae\u7bb1')),
                ('message', models.CharField(max_length=200, verbose_name='\u7559\u8a00')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='article.Article', verbose_name='\u6587\u7ae0')),
            ],
            options={
                'verbose_name': '\u8bc4\u8bba\u8868',
                'verbose_name_plural': '\u8bc4\u8bba\u8868',
            },
        ),
    ]
