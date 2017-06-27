# -*- coding:utf-8 -*-
# __author__ = 'lgh'
# __date__ = '2017/6/27 0027'

from django.conf.urls import url
from views import IndexView, DetailView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^(?P<article_id>\d+)/$', DetailView.as_view(), name='detail'),
]