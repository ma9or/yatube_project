from django.urls import path

from . import views

urlpatterns = [
    #главная страница
    path('', views.index),
    #страница списка постов
    path('group/', views.group_posts_list),
    #slug(это строка из букв и цифр)
    path('group/<slug:slug>/', views.group_posts_detail),
] 