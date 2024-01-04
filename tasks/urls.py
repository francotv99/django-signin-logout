from django.urls import path,include
#from myapp.views import hello
#otra forma de importar es
from . import views 

urlpatterns = [ 
    path('',views.home, name="home"),
    path('signup/',views.signup, name="signup"),
    path('tasks/',views.tasks, name="tasks"),
    path('tasks_done/',views.tasks_done, name="tasks_done"),
    path('logout/',views.signout, name="logout"),
    path('signin/',views.signin, name="signin"),
    path('tasks/create',views.create_task, name="create_task"),
    # se colocara un dato dinamico
    path('tasks/<int:task_id>',views.task_detail, name="task_detail"),
    path('tasks/<int:task_id>/complete',views.complete_task, name="complete_task"),
    path('tasks/<int:task_id>/delete',views.delete_task, name="delete_task")
]