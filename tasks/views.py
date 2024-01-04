from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
#Este formulario sirve para la creacion de formulario
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
#Libreria del cual guarda usuarios
from django.contrib.auth.models import User
#Crea la cookie en google
from django.contrib.auth import login,logout,authenticate
#Asignar a un error especifico
#Este es para un error de que indica que se repite el usuario
from django.db import IntegrityError

#Se importara el formulario que se creo de forms.py
from .forms import TaskForm

# se importara la tabla task
from .models import Task

from django.utils import timezone


from django.contrib.auth.decorators import login_required



# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):
    ##Una diferencia entre si subio el formualrio o no:
    if request.method =='GET':
        print("enviando formulario")
        return render(request,'signup.html',{
        'form':UserCreationForm#crea formularios para crear usuario
    })
    else:
        print("obteniendo datos")
        if request.POST['password1']==request.POST['password2']:
            try:
                #se guarda en base de datos:user
                user= User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('tasks')
            except IntegrityError:
                return render(request,'signup.html',{
                'form':UserCreationForm,#crea formularios para crear usuario
                'error':'User name already exist'
                })

           
        return render(request,'signup.html',{
                'form':UserCreationForm,#crea formularios para crear usuario
                'error':'Password do not match'
                })
#Pagina de Tareas
@login_required
def tasks(request):
    #todas las tareas:
    #task=Task.objects.all()
    
    #datecompleted__isnull es para ver si la tarea sigue incompelta
    
    #Filtra tareas solamnete del autor
    task=Task.objects.filter(user=request.user,datecompleted__isnull=True)
    return render(request,'tasks.html',{
        'task':task
    })

#Mostrar tareas completadas en otra pagina
def tasks_done(request):
    #todas las tareas:
    #task=Task.objects.all()
    
    #datecompleted__isnull es para ver si la tarea sigue incompelta
    
    #Filtra tareas solamnete del autor
    task=Task.objects.filter(user=request.user,datecompleted__isnull=False).order_by('datecompleted')
    return render(request,'tasks.html',{
        'task':task
    })
#Crea Tarea
@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request,'create_task.html',{
        'form':TaskForm
    })
    else:
        try:
            #Con task form es como que se crea el formulario con las variaobles de
            #del formulario real y se exportan
            form=TaskForm(request.POST)
            new_task=form.save(commit=False)
            new_task.user=request.user
            new_task.save()
            return redirect ('tasks')
        except ValueError:
            return render(request,'create_task.html',{
            'form':TaskForm,
            'error':'Por favor prove un dato valido'
            })
#Edita tarea      
@login_required    
def task_detail(request,task_id):
    if request.method=='GET':
        task=get_object_or_404(Task, pk=task_id,user=request.user)
        form=TaskForm(instance=task)
        return render (request,'task_detail.html',{
        'task':task,
        'form':form
        })
    else:
        try:
            task=get_object_or_404(Task, pk=task_id,user=request.user)
            form=TaskForm(request.POST,instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render (request,'task_detail.html',{
            'task':task,
            'form':form,
            'error':'Error actualizando task'
             })
            
#Actuliazar Estado de tarea
@login_required
def complete_task(request,task_id):
    task=get_object_or_404(Task,pk=task_id,user=request.user)
    if request.method=='POST':
        task.datecompleted=timezone.now()
        task.save()
        return redirect('tasks')
#Eliminar Tarea
@login_required
def delete_task(request,task_id):
    task=get_object_or_404(Task,pk=task_id,user=request.user)
    if request.method=='POST':
        task.delete()
        return redirect('tasks')

        
        
@login_required
def signout(request):
    logout(request)
    return redirect('home')
def signin(request):
    #verifica si es actualizacion de la pagina o envio del formulario
   if request.method=='GET':
       return render(request,'signin.html',{
      'form':AuthenticationForm  
    })
   else:
       #aqui compara en la con la base de datos con authenticate 
       user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
       if user is None:
            return render(request,'signin.html',{
      'form':AuthenticationForm, 
      'error':'User name or password is incorrect'
    })
       else:
           #login sirve para guardar la sesion
           login(request,user)
           return redirect('tasks')
  
        
       

        
    