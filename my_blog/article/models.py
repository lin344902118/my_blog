# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'博客标题')
    category = models.CharField(max_length=50, blank=True, null=True, verbose_name=u'博客标签')
    date_time = models.DateTimeField(auto_now_add=True, verbose_name=u'博客日期')
    content = models.TextField(blank=True, null=True, verbose_name=u'博客内容')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'博客文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_time']


class Comment(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'姓名')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    message = models.CharField(max_length=200, verbose_name=u'留言')
    article = models.ForeignKey(Article, related_name='comment', verbose_name=u'文章')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'评论表'
        verbose_name_plural = verbose_name