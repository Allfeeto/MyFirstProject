from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm


def index(request):
    if request.method == 'POST':
        # Передаем данные в форму
        userform = UserForm(request.POST, request.FILES)
        if userform.is_valid():
            # Если форма валидна, извлекаем данные
            cleaned_data = userform.cleaned_data

            # Пример вывода данных
            output = f"""
                <h2>Пользователь</h2>
                <h3>
                    Имя: {cleaned_data['name']} <br>
                    Возраст: {cleaned_data['age']} <br>
                    Электронная почта: {cleaned_data['email']} <br>
                    Телефон: {cleaned_data['RF']} <br>
                    Положить в корзину: {'Да' if cleaned_data['basket'] else 'Нет'} <br>
                    Зачтете лабораторную: {'Да' if cleaned_data['vyb'] else 'Нет'} <br>
                    Ссылка на соцсети: {cleaned_data['url_text']} <br>
                    Файл: {cleaned_data['file_path']} <br>
                    Загруженный файл: {cleaned_data['file']}, Загруженное изображение: {cleaned_data['image']} <br>
                    Дата: {cleaned_data['data_field']} <br>
                    Целое число: {cleaned_data['integer_field']} <br>
                    Выбор: {cleaned_data['choice_field']}
                </h3>
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

