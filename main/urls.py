from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('update', views.update, name='upate'),
    path('<str:ticker>/', views.summary, name='summary'),
    # path('list', views.companyList, name = 'List'),
]   
