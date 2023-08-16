from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about),
    path('hello/<str:username>', views.hello),
    path('operation/<int:number>', views.operation),
    path('projects/', views.projects, name='projects'),
    path('tasks/', views.tasks, name='tasks'),
    path('create_task/', views.create_task, name='create_task'),
    path('create_project/', views.create_project, name='create_project'),
    path('tasks_project/<int:project_id>', views.tasks_project),
]