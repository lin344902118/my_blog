# -*- coding:utf-8 -*-
# __author__ = 'lgh'
# __date__ = '2017/6/27 0027'

import xadmin
from xadmin import views

class BaseSetting(object):
    # 主体修改
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    # 整体配置
    site_title = u'博客后台管理系统'
    site_footer = u'lgh个人博客'
    # 收起菜单项
    menu_style = 'accordion'


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)