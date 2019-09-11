from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('filter/', views.filter, name='filter'),
    path('update', views.update, name='update'),
    path('<str:ticker>/', views.summary, name='summary'),
]   
