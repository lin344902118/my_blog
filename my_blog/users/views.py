# -*- coding:utf-8 -*-

from django.shortcuts import render, HttpResponsePermanentRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.views.generic.base import View
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.core.urlresolvers import reverse

from models import UserProfile
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


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            password = request.POST.get('password', '')
            # 上面的 authenticate 方法 return user
            user = authenticate(username=user_name, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponsePermanentRedirect(reverse('index'))
                return render(request, 'login.html', {'msg': '用户未激活！'})
            return render(request, 'login.html', {'msg': '用户名或者密码错误！'})
        return render(request, 'login.html', {'form_errors': login_form.errors})
