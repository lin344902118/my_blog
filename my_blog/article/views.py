# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from models import Article,Comment
from forms import CommentForm

# Create your views here.
class HomeView(View):
    def get(self, request):
        articles = Article.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        except EmptyPage:
            page =1
        p = Paginator(articles, per_page=3, request=request)
        articles = p.page(page)
        return render(request, 'home.html', {'post_list': articles})


class DetailView(View):
    def get(self, request, article_id):
        article = Article.objects.get(id=int(article_id))
        comments = Comment.objects.filter(article=article)
        return render(request, 'detail.html', {'article': article, 'comments': comments})


class CommentView(View):
    def post(self, request):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = Comment()
            comment.name = comment_form.cleaned_data['name']
            comment.email = comment_form.cleaned_data['email']
            comment.message = comment_form.cleaned_data['message']
            comment.article_id = request.POST.get('article_id')
            comment.save()
            msg = u'提交成功'
        else:
           msg = comment_form.errors
        return render(request, 'detail.html', {"response": msg})


class SearchView(View):
    def get(self, request):
        keyword = request.GET.get('keyword', '')
        if keyword:
            articles = Article.objects.filter(
                Q(title__icontains=keyword) |
                Q(category__icontains=keyword) |
                Q(content__icontains=keyword)
            )
        else:
            articles = Article.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        except EmptyPage:
            page =1
        p = Paginator(articles, per_page=3, request=request)
        articles = p.page(page)
        return render(request, 'home.html', {'post_list': articles})

