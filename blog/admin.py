from django.contrib import admin

from blog.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'get_short_text')  # Отображаем заголовок, пользователя и короткий текст
    list_filter = ('user',)  # Добавляем фильтр по полю user
    search_fields = ('title',)

admin.site.register(Article, ArticleAdmin)
# Register your models here.
