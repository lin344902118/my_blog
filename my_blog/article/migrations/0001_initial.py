# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-27 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u535a\u5ba2\u6807\u9898')),
                ('category', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u535a\u5ba2\u6807\u7b7e')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='\u535a\u5ba2\u65e5\u671f')),
                ('content', models.TextField(blank=True, null=True, verbose_name='\u535a\u5ba2\u5185\u5bb9')),
            ],
            options={
                'ordering': ['-date_time'],
                'verbose_name': '\u535a\u5ba2\u6587\u7ae0',
                'verbose_name_plural': '\u535a\u5ba2\u6587\u7ae0',
            },
        ),
    ]