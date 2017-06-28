# -*- coding:utf-8 -*-
# __author__ = 'lgh'
# __date__ = '2017/6/27 0027'

from django.conf.urls import url
from views import HomeView, DetailView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),

    url(r'^(?P<article_id>\d+)/$', DetailView.as_view(), name='detail'),
]