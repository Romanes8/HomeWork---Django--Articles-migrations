from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    articles = Article.objects.all()
    template = 'articles/news.html'
    context = {
        'object_list': articles
    }
    ordering = '-published_at'
    return render(request, template, context)
