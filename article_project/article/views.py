from django.shortcuts import render, get_object_or_404

from article.models import Article, Comments


def index(request):
    a = Article.objects.all()
    context = {'articles': a}
    return render(request, 'article/index.html', context)

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    com = Comments.objects.filter(name_art_id=article)

    context = {
        'article': article,
        'com': com

    }
    return render(request, 'article/detail.html', context)