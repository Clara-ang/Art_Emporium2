from django.db import models
from django.contrib.auth.models import User



class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    telefone = models.CharField("Telefone", max_length = 19, null = True)

# Create your models here.


class Base(models.Model):
    creation = models.DateField("Data de criação", auto_now_add=True)
    modified = models.DateField("Data de atualização", auto_now= True)
    active = models.BooleanField("Ativo?", default= True)


#Criando um perfil e adicionando campos ao meu usuário
  
class Personal(Base):
    #Campos Adicionais   
    phone_number = models.CharField("Telefone", max_length=100, null= True) #permitir ser nulos na criação
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.user.email  


