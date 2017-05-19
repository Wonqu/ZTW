from django.shortcuts import render
from django.http import HttpResponseRedirect
from Prosaist.view_scripts.forms.entity import EntityCreateForm
from Prosaist.models import Entity, Project, User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from Prosaist.text import messages as msg


def view(request, username, projectname):
    user_id = User.objects.get(username=username)
    project = Project.objects.get(name=projectname, pr_owner_id=user_id)
    project_id = project.id
    form = EntityCreateForm(initial={'project' : project_id})
    form.fields['project'].disabled = True
    if request.method == 'POST':
        form = EntityCreateForm(request.POST)
        if(form.is_valid()):
            try:
                name = request.POST.get('name','')
                entity = Entity(en_project=project,name=name)
                entity.save()
                messages.add_message(request, messages.SUCCESS, msg.message_entity_success)
            except ObjectDoesNotExist:
                messages.add_message(request, messages.ERROR, msg.message_entity_error)
            return HttpResponseRedirect('.')
    return render(request, "inputform.html", {'form' : form, 'username' : username, 'projectname' : projectname})
