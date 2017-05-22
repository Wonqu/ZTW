from django.shortcuts import render
from Prosaist.models import Project, User


def view(request, username, projectname, model):
    user_id = User.objects.get(username=username)
    project = Project.objects.get(name=projectname, owner_id=user_id)
    project_id = project.id
    objects = model.objects.filter(project_id=project_id)
    return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname})
