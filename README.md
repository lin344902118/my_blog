# my_blog
# 该项目是个简单的博客系统，参考了极客学院的python中的简易博客开发文章
该项目集成了xadmin，django-pure-pagination可以通过登录xadmin在后台添加博客，然后显示，并可以查看详情,添加评论，搜索博文，分页。对详情页做了markdown
后期要开发的功能有注册和登录(会使用到验证码)以及个人信息的修改包括昵称，地址，头像等等。暂时就想到这些有时间继续拓展
首页和博客页都是从网上找的模板，而且使用了bootstrap的一些样式。
django本身有pagnator但是不支持搜索翻页(需要修改url)，django-pure-pagination支持搜索翻页