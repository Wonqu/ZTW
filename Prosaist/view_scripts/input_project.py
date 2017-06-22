from django.shortcuts import render
from django.http import HttpResponseRedirect
from Prosaist.models import Project, User
from Prosaist.view_scripts.forms.project import ProjectCreateForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from Prosaist.text.messages import message_project_success, message_project_error


def view_base(request, username):
    if request.user.is_authenticated:
        user_id = User.objects.get(username=username)
        form = ProjectCreateForm()
        name = ''
        if request.method == 'POST':
            form = ProjectCreateForm(request.POST)
            if (form.is_valid()):
                try:
                    name = request.POST.get('name', '')
                    object = Project(name=name)
                    object.save()
                    messages.add_message(request, messages.SUCCESS, message_project_success)
                except ObjectDoesNotExist:
                    messages.add_message(request, messages.ERROR, message_project_error)
                return HttpResponseRedirect('.')
        return HttpResponseRedirect('.' + name + '/')
    else:
        return HttpResponseRedirect('/prosaist/')
