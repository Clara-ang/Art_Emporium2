from email.header import Header
from django.urls import path
from .views import ContatoView, HomeView, LojasView, ServicosView, PortfólioViews, SomosView, HeaderView

urlpatterns = [
    path('', HomeView.as_view(), name= 'home'), 
    path('portfolio/', PortfólioViews.as_view()),
    path('contato/', ContatoView.as_view()), 
    path('serviços/', ServicosView.as_view()),
    path('somos/', SomosView.as_view()),
    path('lojas/', LojasView.as_view()),
    path('header/', HeaderView.as_view(),)
]