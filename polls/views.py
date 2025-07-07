from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Avg
from .models import Project, Vote

def project_list(req):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(req, 'polls/project_list.html', context)

def project_detail(req, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {'project': project}

    if req.method == 'POST':
        score = int(req.POST.get('score'))
        Vote.objects.create(project=project, score=score)
        return redirect('project_result', pk=pk)
    
    return render(req, 'polls/project_detail.html', context)

def project_result(request, pk):
    project = get_object_or_404(Project, pk=pk)
    votes = Vote.objects.filter(project=project)
    avg_score = votes.aggregate(avg=Avg('score'))['avg']
    vote_count = votes.count()
    return render(request, 'polls/project_result.html', {
        'project': project,
        'avg_score': avg_score,
        'vote_count': vote_count,
    })