from django.contrib import admin
#se llama desde el archivo models la tabla Task
from .models import Task

# Register your models here.

#Esta clase es para que se muetre en el fomrulario de django
#Para que created de models.py se vea en el formulario 
class TaskAdmin(admin.ModelAdmin):
    readonly_fields=("created",)

##Vincular la tabla con el programa en este 

admin.site.register(Task, TaskAdmin)
