from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask
from .forms import CreateNewProject

def index( request ):
    title = "Django Project!!"
    return render(request, 'index.html', {
        'title': title
    })

def hello( request, username ):
    print(username)
    return HttpResponse('Hello %s' % username)

def about( request ):
    return HttpResponse('<h1>About us</h1>')

def operation( request, number ):
    result = (number + 100) * 2
    return HttpResponse('<h2>El resultado de (%s + 100) * 2 es %s </h2>' % (number, result))

# Listando todos los proyectos
def projects( request ):
    title = 'Projects'
    projects = list(Project.objects.values())
    return render(request, 'projects/projects.html', {
        'title': title,
        'projects': projects
    })
def create_project( request ):
    if request.method == 'GET':    
        return render( request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else: 
        name = request.POST['name']
        Project.objects.create(name=name,)
        return redirect('/projects')

# Listar una tarea
def tasks( request ):
    # task = Task.objects.get(id=id)
    # task = get_object_or_404(Task, id=id)
    # return HttpResponse("<h1>Task: %s</h1>" % task.title)
    tasks = Task.objects.all()
    return render( request, 'tasks/tasks.html', {
        'tasks': tasks
    })

def create_task( request ):
    if request.method == 'GET':    
        return render( request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else: 
        title = request.POST['title']
        description = request.POST['description']
        project_id = request.POST['project_id']
        Task.objects.create(title=title, description=description, project_id=project_id)
        return redirect('/tasks')
    
def tasks_project(request, project_id):
    project = Project.objects.get(id=project_id)
    tasks = Task.objects.all().filter(project_id = project_id)
    return render(request,'projects/tasks.html', {
        'project': project.name,
        'tasks': tasks
    })