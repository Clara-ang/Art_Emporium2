from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect


from .models import Personal as Personal

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
        
        user = User.objects.filter(username = username).first()   
        if user:
            return render(request, "base/pages/permission.html")
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        Personal.objects.create(user= user)  #cria o perfil do usuário após o cadastro
        return render(request, "base/pages/home.html")

def login(request):
    if request.method == 'GET':
        return render(request, "base/pages/register.html")
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login_django(request, user)
            return redirect('home2')         
        else:
            return HttpResponseRedirect(reverse('register')) 

#página principal logado no site  

@login_required  
class Home2View(TemplateView):
    template_name = 'base/pages/home2.html'

@login_required 
class Personal(TemplateView):
    template_name = 'base/pages/personal.html' 
