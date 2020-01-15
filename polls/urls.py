from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('polls1',views.polls1,name='polls1'),
]