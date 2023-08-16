from django import forms
from .models import Project

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Task title", max_length=200)
    description = forms.CharField(label="Task description", widget=forms.Textarea)

    # CHOICES = (('Option 1', 'Option 1'), ('Option 2', 'Option 2'))
    # project_id = forms.CharField(label="Project ID", widget=forms.Select(choices = CHOICES))

    CHOICES = Project.objects.all()
    project_id = forms.ModelChoiceField(label="Project", queryset = CHOICES)


class CreateNewProject(forms.Form):
    name = forms.CharField(label="Project title", max_length=50)
