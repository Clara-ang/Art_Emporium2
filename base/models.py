from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    creation = models.DateField("Data de criação", auto_now_add=True)
    modified = models.DateField("Data de atualização", auto_now= True)
    active = models.BooleanField("Ativo?", default= True)
    
    class Meta:
        abstract = True

#Criando um perfil e adicionando campos ao meu usuário
class Personal(Base):
    #Campos Adicionais   
    phone_number = models.CharField("Telefone", max_length=100, null= True) #permitir ser nulos na criação
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.user.email  



