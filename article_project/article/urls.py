
from django.contrib import admin
from django.urls import path

from article import views
from article.views import index, detail, date_time_filter, search_theme, index_slug

app_name = 'article'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('date_filter/', date_time_filter, name='date_filter'),
    path('index_filter/', search_theme, name='index_filter'),
    path('index_slug/<slug>', index_slug)

]