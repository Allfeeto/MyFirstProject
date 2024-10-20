from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Первый проект на django")
def about(request):
    return HttpResponse("<h2>О сайте</h2>")
def contact(request):
    return HttpResponse("<h2>Контакты</h2>")
# Create your views here.
def products(request, productid=1):
    output = "<h2>Продукт № {0}</h2>".format(productid)
    return HttpResponse(output)
def users(request, id, name):
    output = "<h2>Пользователь</h2> <h3>id: {0} - Имя {1}</h3>".format(id, name)
    return HttpResponse(output)