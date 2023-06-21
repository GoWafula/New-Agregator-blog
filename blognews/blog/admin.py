from django.contrib import admin
from .models import Article
# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    list_filter = ('author', 'pub_date')
    search_fields = ('title', )
    ordering = ('-pub_date',)

    readonly_fields = ('url',)
