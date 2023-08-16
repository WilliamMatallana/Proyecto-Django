from django.db import models

class Project(models.Model):
    '''
    Modelo que representa un proyecto
    '''
    name = models.CharField(max_length=50, help_text='Ingrese el nombre del proyecto.')

    def __str__(self):
        return self.name

class Task(models.Model):
    '''
    Modelo que respresenta una tarea de un proyecto
    '''
    title = models.CharField(max_length=200, help_text='Ingrese el título de la tarea.')
    description = models.TextField(help_text='Ingrese la descripción de la tarea.')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title + ' - ' + self.project.name