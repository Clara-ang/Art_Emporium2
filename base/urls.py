from django.urls import path
from .views import ContatoView, HomeView, LojasView, QuemsView, ServicosView, PortfólioViews

urlpatterns = [
    path('', HomeView.as_view(), name= 'home'), 
    path('portfolio/', PortfólioViews.as_view()),
    path('', QuemsView.as_view(), name= 'quem'),
    path('contato/', ContatoView.as_view()), 
    path('serviços/', ServicosView.as_view()),

]