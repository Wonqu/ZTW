from django.shortcuts import render
from django.http import HttpResponseRedirect
from Prosaist.view_scripts.forms.event import EventCreateForm
from Prosaist.models import Event, Project


def view(request):
    if request.method == 'POST':
        form = EventCreateForm(request.POST)
        if(form.is_valid()):
            project_id = request.POST.get('project','')
            project = Project.objects.get(id=project_id)
            name = request.POST.get('name','')
            event = Event(ev_project=project,name=name)
            event.save()
            return HttpResponseRedirect('.')
    else:
        form = EventCreateForm()
    return render(request, "inputform.html", {'form' : form})