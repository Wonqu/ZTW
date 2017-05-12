from django.shortcuts import render
from django.http import HttpResponseRedirect
from Prosaist.view_scripts.forms.category import CategoryCreateForm
from Prosaist.models import Category, Project


def view(request):
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if(form.is_valid()):
            project_id = request.POST.get('project','')
            project = Project.objects.get(id=project_id)
            name = request.POST.get('name','')
            category = Category(ct_project=project,name=name)
            category.save()
            return HttpResponseRedirect('.')
    else:
        form = CategoryCreateForm()
    return render(request, "inputform.html", {'form' : form})