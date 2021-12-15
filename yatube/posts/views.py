# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')


# Страница со списком постов
def group_posts_list(request):
    return HttpResponse('Список постов')


# Страница с информацией об ;
# view-функция принимает параметр slug из path()
def group_posts_detail(request, slug):
    return HttpResponse(f'Номер поста {slug}') 
