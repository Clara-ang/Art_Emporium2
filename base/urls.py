from django.urls import path
from .views import ContatoView, HomeView, Home2View, LojasView, Personal, ServicosView, PortfólioViews, SomosView, MenuView, register, login



urlpatterns = [
    path('', HomeView.as_view(), name= 'home'), 
    path('portfolio/', PortfólioViews.as_view()),
    path('', ContatoView.as_view(), name= 'contato'), 
    path('serviços/', ServicosView.as_view()),
    path('', SomosView.as_view(), name= 'somos'),
    path('lojas/', LojasView.as_view()),
    path('menu/', MenuView.as_view()),

    #autenticação
    path('register/', register, name = 'register'),
    path('login/', login, name = 'login'),

    #páginas logado
    path('home2/', Home2View, name = 'home2'),
    path('perfil/', Personal, name = 'perfil'),
]