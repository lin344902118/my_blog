# -*- coding:utf-8 -*-
# __author__ = 'lgh'
# __date__ = '2017/6/29 0029'

from django import forms
from models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']