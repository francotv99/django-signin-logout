from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#creamos nuetra propia tabla 
class Task(models.Model):
    #charfiel para texto corto
    title=models.CharField(max_length=100)
    #textfiel para texto largo, blank es que por defecto campo vacio
    description=models.TextField(blank=True)
    #Date time field con auto now crea por defecto para ver cuando la ha creado
    created=models.DateTimeField(auto_now_add=True)#Automica fecha
    #Date time field con null es para marcar la fecha
    datecompleted=models.DateTimeField(null=True)# Puede estar vacio
    #Boolfield es para defeinir entre verdadero o falso
    important=models.BooleanField(default=False)
    #Lo que se hara creara otra tabla con los datos de usuario
    #foreingkey es para entre relacionar la tabla en este caso con USEr 
    #la que regustraba usuarios:
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    #hace que se muetre en el panel con su nombre
    def __str__(self):
        return self.title + '- by '+self.user.username