from django.contrib import admin

from blog.models import Article, Comment

# Register your models here.
class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'get_short_text')  # Отображаем заголовок, пользователя и короткий текст
    list_filter = ('user',)  # Добавляем фильтр по полю user
    search_fields = ('title',)
    inlines = [
        CommentInline,
    ]

admin.site.register(Article, ArticleAdmin)


