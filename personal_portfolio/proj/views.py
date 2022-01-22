from django.shortcuts import render
from proj.models import Project

def project_index(request):
    projects = Pro.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)
def project_details(request):
    project = Pro.object.all(pk = pk)
    context  = {
        'project':project
    }
    return render(request,project_details.html,context)