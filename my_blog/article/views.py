from django.shortcuts import render
from django.views.generic.base import View
from models import Article

# Create your views here.
class HomeView(View):
    def get(self, request):
        articles = Article.objects.all()
        return render(request, 'home.html', {'post_list': articles})


class DetailView(View):
    def get(self, request, article_id):
        article = Article.objects.get(id=int(article_id))
        return render(request, 'detail.html', {'post': article})

