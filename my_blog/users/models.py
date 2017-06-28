# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称', default='')
    birthday = models.DateField(null=True, blank=True, verbose_name=u'生日')
    sex = models.CharField(max_length=6, choices=(('male', u'男'), ('female', u'女')), default='male', verbose_name=u'性别')
    address = models.CharField(max_length=100, default='', verbose_name=u'地址')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u'手机号')
    image = models.ImageField(max_length=100, upload_to='image/%Y/%m', default='default.png', verbose_name=u'头像')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name


class LeaveMessage(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'姓名')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    message = models.CharField(max_length=200, verbose_name=u'留言')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'留言表'
        verbose_name_plural = verbose_name