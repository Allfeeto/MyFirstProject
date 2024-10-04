from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from blog.forms import *
from blog.models import Article
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def home(request):
    article = Article.objects.all()
    context = {
        'articles': article
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')

def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/article.html', {'article': article})



# страница пользователя
def me(request):
    # если не авторизован, то редирект на страницу входа
    if not request.user.is_authenticated:
        return redirect('login')
    # рендерим шаблон и передаем туда объект пользователя
    return render(request, 'blog/me.html', {'user': request.user})

# выход
def doLogout(request):
    # вызываем функцию django.contrib.auth.logout и делаем редирект на страницу входа
    logout(request)
    return redirect('login')

# страница входа
def loginPage(request):

    # инициализируем объект класса формы
    form = LoginForm()

    # обрабатываем случай отправки формы на этот адрес
    if request.method == 'POST':

        # заполянем объект данными, полученными из запроса
        form = LoginForm(request.POST)

        # проверяем валидность формы
        if form.is_valid():
            # пытаемся авторизовать пользователя
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                # если существует пользователь с таким именем и паролем,
                # то сохраняем авторизацию и делаем редирект
                login(request, user)
                return redirect('me')
            else:
                # иначе возвращаем ошибку
                form.add_error(None, 'Неверные данные!')

    # рендерим шаблон и передаем туда объект формы
    return render(request, 'blog/login.html', {'form': form})

# регистрация
def registerPage(request):

    # инициализируем объект формы
    form = RegisterForm()

    if request.method == 'POST':
        # заполняем объект данными формы, если она была отправлена
        form = RegisterForm(request.POST)

        if form.is_valid():
            # если форма валидна - создаем нового пользователя
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('login')
    # ренедерим шаблон и передаем объект формы
    return render(request, 'blog/registration.html', {'form': form})
