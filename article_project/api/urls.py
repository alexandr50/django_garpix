from django.urls import path
from .views import ArticleView, CommentView, ArticleViewset, CommentViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('articles2', ArticleViewset)
router.register('comments2', CommentViewset)

urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('comments/', CommentView.as_view()),
]

urlpatterns += router.urls