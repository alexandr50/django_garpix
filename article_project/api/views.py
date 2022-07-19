from article.models import Article, Comments
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ArticleSerializer, CommentSerializer
from rest_framework import viewsets


class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({'articles': serializer.data})

    def post(self, request):
        article = request.data.get('article')
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            saved_data = serializer.save()
        return Response({'success': "Article, '{}': created successfuly".format(saved_data.name)}, status=201)






class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentView(APIView):
    def get(self, request):
        comments = Comments.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response({'comments': serializer.data})

    def post(self, request):
        comment = request.data.get('comment')
        serializer = CommentSerializer(data=comment)
        if serializer.is_valid(raise_exception=True):
            saved_data = serializer.save()
        return Response({'success': "Comment, '{}': created successfuly".format(saved_data.name)}, status=201)


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer