# -*- coding:utf-8 -*-
# __author__ = 'lgh'
# __date__ = '2017/6/27 0027'

from django.conf.urls import url
from views import HomeView, DetailView, SearchView, CommentView

urlpatterns = [
    #首页
    url(r'^$', HomeView.as_view(), name="home"),
    #详情页
    url(r'^(?P<article_id>\d+)/$', DetailView.as_view(), name='detail'),
    #提交评论
    url(r'^comment', CommentView.as_view(), name='comment'),
    #搜索
    url(r'^search', SearchView.as_view(), name='search')
]