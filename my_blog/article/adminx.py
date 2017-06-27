# -*- coding:utf-8 -*-
# __author__ = 'lgh'
# __date__ = '2017/6/27 0027'

import xadmin
from xadmin import views
from models import Article

class ArticleAdmin(object):
    list_display = ['title', 'category', 'date_time', 'content']
    search_fields = ['title', 'category', 'content']
    list_filter = ['title', 'category', 'content']

xadmin.site.register(Article, ArticleAdmin)