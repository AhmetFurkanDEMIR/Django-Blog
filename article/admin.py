from django.contrib import admin
from .models import Article

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    class Meta:
        model = Article

    list_display = ["title", "author", "created_date"]

    list_display_links = ["title", "created_date"]

    search_fields = ["title"]

    list_filter = ["created_date"]