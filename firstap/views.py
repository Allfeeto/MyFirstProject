from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm


def index(request):
    if request.method == 'POST':
        # Передаем данные в форму
        userform = UserForm(request.POST, request.FILES)
        if userform.is_valid():
            # Если форма валидна, извлекаем данные
            name = userform.cleaned_data['name']
            age = userform.cleaned_data['age']
            email = userform.cleaned_data['email']
            phone = userform.cleaned_data['RF']

            # Здесь можно обработать файлы
            uploaded_file = request.FILES.get('file')
            uploaded_image = request.FILES.get('image')

            # Пример вывода данных
            output = f"""
                <h2>Пользователь</h2>
                <h3>Имя: {name} <br> Возраст: {age} <br> Электронная почта: {email} <br> Телефон: {phone}</h3>
            """
            return HttpResponse(output)
    else:
        # Инициализируем пустую форму при GET-запросе
        userform = UserForm()

    # Рендерим шаблон и передаем форму
    return render(request, 'index.html', {'form': userform})


def about(request):
    return HttpResponse("<h2>О сайте</h2>")


def contact(request):
    return HttpResponse("<h2>Контакты</h2>")


# Create your views here.
def products(request, productid=1):
    output = "<h2>Вы выбрали продукт № {0}</h2>".format(productid)
    return HttpResponse(output)


def users(request, id, name):
    output = "<h2>Вы выбрали пользователя</h2> <h3>id: {0} Имя: {1}</h3>".format(id, name)
    return HttpResponse(output)


# python manage.py runserver

