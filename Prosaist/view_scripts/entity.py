from django.shortcuts import render
from django.http import HttpResponseRedirect
from Prosaist.view_scripts.forms.entity import EntityCreateForm
from Prosaist.models import Entity, Project


def view(request):
    if request.method == 'POST':
        form = EntityCreateForm(request.POST)
        if(form.is_valid()):
            project_id = request.POST.get('project','')
            project = Project.objects.get(id=project_id)
            name = request.POST.get('name','')
            entity = Entity(en_project=project,name=name)
            entity.save()
            return HttpResponseRedirect('.')
    else:
        form = EntityCreateForm()
    return render(request, "inputform.html", {'form' : form})
