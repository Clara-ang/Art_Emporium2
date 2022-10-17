from http.client import HTTPResponse
from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User



class HomeView(TemplateView):
    template_name = "base/pages/home.html"

class PortfólioViews(TemplateView):
    template_name = "base/pages/portfolio.html"

class ContatoView(TemplateView):
    template_name = "base/pages/contato.html"

class ServicosView(TemplateView):
    template_name = "base/pages/serviços.html"

class LojasView(TemplateView):
    template_name = "base/pages/lojas.html"

class SomosView(TemplateView):
    template_name = "base/pages/somos.html"

class HeaderView(TemplateView):
    template_name = "base/pages/header"
    
class MenuView(TemplateView):
    template_name = "base/components/menu.html"    


def register(request):
    if request.method == 'GET':
        return render(request, "base/pages/register.html")
    
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        #user = User.objects.filter('username').first()
        
        #if user:
        #    return render(request, "core/pages/permisson.html")
        #else:
        user = User.objects.create_user(username=username, email=email, password=password)
        
        return render(request, "base/pages/home.html")



