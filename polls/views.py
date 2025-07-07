from django.shortcuts import render
from .models import Project, Vote

def project_list(req):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(req, 'polls/project_list.html', context)