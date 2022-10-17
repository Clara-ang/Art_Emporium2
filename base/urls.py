from email.header import Header
from django import views
from django.urls import path
from .views import ContatoView, HomeView, LojasView, ServicosView, PortfólioViews, SomosView, MenuView, register
from django.http import HttpResponse


urlpatterns = [
    path('', HomeView.as_view(), name= 'home'), 
    path('portfolio/', PortfólioViews.as_view()),
    path('contato/', ContatoView.as_view()), 
    path('serviços/', ServicosView.as_view()),
    path('somos/', SomosView.as_view()),
    path('lojas/', LojasView.as_view()),
    path('menu/', MenuView.as_view()),

    #autenticação
    path('register/', register, name = 'register'),
]