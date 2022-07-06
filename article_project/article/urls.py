
from django.contrib import admin
from django.urls import path

from article import views
from article.views import index, detail

app_name = 'article'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail')
]