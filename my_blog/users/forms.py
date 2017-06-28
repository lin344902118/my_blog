# -*- coding:utf-8 -*-
# __author__ = 'lgh'
# __date__ = '2017/6/28 0028'

from django import forms
from models import LeaveMessage

class MessageForm(forms.ModelForm):
    class Meta:
        model = LeaveMessage
        fields = ['name', 'email', 'message']