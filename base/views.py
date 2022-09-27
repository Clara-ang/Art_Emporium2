from pipes import Template
from django.views.generic import TemplateView


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