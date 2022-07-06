from django.db import models

# Create your models here.

class Article(models.Model):
    header = models.CharField(max_length=100, verbose_name='заголовок')
    text = models.TextField(max_length=5000, verbose_name='контент')

    def __str__(self):
        return self.header

class Comments(models.Model):
    name_art = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.author} {self.text}'