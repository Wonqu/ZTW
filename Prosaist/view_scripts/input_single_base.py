from django.shortcuts import render
from django.http import HttpResponseRedirect
from Prosaist.models import Project, User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


def view_base(request, username, projectname, model, modelform, msg_success, msg_error):
    user_id = User.objects.get(username=username)
    project = Project.objects.get(name=projectname, owner_id=user_id)
    project_id = project.id
    form = modelform(initial={'project': project_id})
    form.fields['project'].widget.attrs['readonly'] = True
    if request.method == 'POST':
        form = modelform(request.POST)
        if (form.is_valid()):
            try:
                name = request.POST.get('name', '')
                object = model(project=project, name=name)
                object.save()
                messages.add_message(request, messages.SUCCESS, msg_success)
            except ObjectDoesNotExist:
                messages.add_message(request, messages.ERROR, msg_error)
            return HttpResponseRedirect('.')
    return render(request, "inputform.html", {'form': form, 'username': username, 'projectname': projectname})
