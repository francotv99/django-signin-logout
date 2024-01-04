from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        ###se basa en el modelo de la tabla creada
        #en models.py
        model=Task
        fields=['title','description','important']