from django.shortcuts import render

def project_list(req):
    return render(req, 'polls/base.html')