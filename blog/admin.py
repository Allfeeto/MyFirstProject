from django.contrib import admin

from blog.models import Article, Comment, Movie, Customer

# Register your models here.
class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'get_short_text')  # Отображаем заголовок, пользователя и короткий текст
    list_filter = ('user',)  # Добавляем фильтр по полю user
    list_editable = ['user']
    search_fields = ('title',)
    inlines = [
        CommentInline,
    ]

class MovieAdmin(admin.ModelAdmin):
    title = ['release_year', 'title', 'length']
    list_display = ('title', 'release_year')  # Отображаем год выпуска, название и продолжительность
    list_editable = ['release_year'] # Делаем продолжительность редактируемыми
    search_fields = ('title', 'length', 'release_year')  # Поля для поиска: название, продолжительность, год выпуска
    list_filter = ('release_year',)  # Фильтр по году выпуска

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone')
    list_editable = ('last_name', 'phone')  # Делаем фамилию и телефон редактируемыми
    search_fields = ('first_name', 'last_name', 'phone')  # Поля для поиска: имя, фамилия, телефон
    list_filter = ('last_name',)  # Фильтр по фамилии


admin.site.register(Article, ArticleAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Customer, CustomerAdmin)

