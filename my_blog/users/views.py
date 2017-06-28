# -*- coding:utf-8 -*-

from django.shortcuts import render, HttpResponse
from django.views.generic.base import View
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from models import UserProfile
from forms import MessageForm
# Create your views here.

# 用户可以用邮箱登录
# setting中药有对应的配置
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username = username) | Q(email = username))
            if user.check_password(password):
                return user
        except Exception, e:
            return None

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {})

    def post(self, request):
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            message_form.save()
            msg = u'修改成功'
        else:
           msg = message_form.errors
        return render(request, 'index.html', {"response": msg})