from django.shortcuts import get_object_or_404, render
from .models import Project, Vote

def project_list(req):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(req, 'polls/project_list.html', context)

def project_detail(req, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {'project': project}
    
    return render(req, 'polls/project_detail.html', context)