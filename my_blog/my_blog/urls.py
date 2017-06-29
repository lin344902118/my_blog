# -*- coding:utf-8 -*-
"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.static import serve #处理静态文件
import xadmin

from users.views import IndexView, LogoutView
from settings import MEDIA_ROOT

urlpatterns = [
    #xadmin后台管理
    url(r'^xadmin/', xadmin.site.urls),
    #首页
    url(r'^$', IndexView.as_view(), name="index"),
    #退出登录
    url(r'^logout$', LogoutView.as_view(), name='logout'),
    #文章
    url(r'^article/', include('article.urls', namespace='article')),
    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]
