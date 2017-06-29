# -*- coding:utf-8 -*-
# __author__ = 'lgh'
# __date__ = '2017/6/27 0027'

import xadmin
from models import Article, Comment

class ArticleAdmin(object):
    list_display = ['title', 'category', 'date_time', 'content']
    search_fields = ['title', 'category', 'content']
    list_filter = ['title', 'category', 'content']


class CommentAdmin(object):
    list_display = ['name', 'email', 'message', 'article']
    search_fields = ['name', 'email', 'message', 'article']
    list_filter = ['name', 'email', 'message', 'article']

xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Comment, CommentAdmin)