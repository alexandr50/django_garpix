from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from article.models import Article, Comments


def index(request):
    a = Article.objects.all()
    context = {'articles': a}
    return render(request, 'article/index.html', context)

def index_slug(request, slug):
    a = get_object_or_404(Article, slug=slug)
    return HttpResponse(a.header)

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    com = Comments.objects.filter(name_art_id=article)


    context = {
        'article': article,
        'com': com

    }
    return render(request, 'article/detail.html', context)

@login_required
def date_time_filter(request):
    if request.method == 'GET':
        start_date = request.GET.get('start')
        c = None
        if start_date:
            c = Comments.objects.filter(created_at__gte=start_date)
            context = {
                'comments': c,
                'date': start_date
            }

            return render(request, 'article/date_filter.html', context)

@login_required
def search_theme(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        n = None
        if name:
            n = Article.objects.filter(header=name)
            context = {
                'names': n,
                'name_user': name
            }

            return render(request, 'article/index_filter.html', context)











