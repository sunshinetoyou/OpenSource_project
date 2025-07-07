from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
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

def admin_dashboard(request):
    projects = Project.objects.annotate(
        avg_score=Avg('vote__score'),
        vote_count=Count('vote')
    ).order_by('-avg_score')
    return render(request, 'polls/admin_dashboard.html', {'projects': projects})

@receiver([post_save, post_delete], sender=Vote)
def update_project_avg_score(sender, instance, **kwargs):
    project = instance.project
    avg = project.vote_set.aggregate(avg=Avg('score'))['avg']
    project.avg_score = avg
    project.save(update_fields=['avg_score'])