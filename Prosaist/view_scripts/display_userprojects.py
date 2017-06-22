from django.shortcuts import render
from django.http import HttpResponseRedirect
from Prosaist.models import Project, User
from Prosaist.view_scripts.forms.project import ProjectCreateForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from Prosaist.text.messages import message_project_success, message_project_error


def view(request, username):
    if request.user.is_authenticated:
        user_id = User.objects.get(username=username).id
        projects = Project.objects.filter(owner_id=user_id)
        newProject = ProjectCreateForm()
        if request.method == 'POST':
            form = ProjectCreateForm(request.POST)
            if (form.is_valid()):
                try:
                    name = request.POST.get('name', '')
                    object = Project(name=name, owner_id=user_id)
                    object.save()
                    messages.add_message(request, messages.SUCCESS, message_project_success)
                    return HttpResponseRedirect(name + '/')
                except ObjectDoesNotExist:
                    messages.add_message(request, messages.ERROR, message_project_error)
        return render(request, "inputform.html", {'form': newProject, 'data': projects, 'username': username})
    else:
        return HttpResponseRedirect('/prosaist/')