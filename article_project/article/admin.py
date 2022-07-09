from django.contrib import admin

# Register your models here.
from article.models import Article,  Comments

admin.site.register(Comments)


class CommentsAdminInline(admin.TabularInline):
    model = Comments
    fk_name = 'name_art'
    extra = 5

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentsAdminInline]