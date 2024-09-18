from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import *

class HomeView(ListView):
    context_object_name = 'project_list'
    model = Project
    template_name = "mycontent/home.html"

class AboutView(TemplateView):
    template_name = "mycontent/about.html"

class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'description']
    template_name = "mycontent/create.html"
    success_url ="/"

class ProjectEditView(UpdateView):
    model = Project
    fields = ['name','description']
    template_name = "mycontent/create.html"
    success_url ="/"

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "mycontent/delete.html"
    fields = ['name']
    success_url ="/"