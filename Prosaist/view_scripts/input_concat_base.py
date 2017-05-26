from django.shortcuts import render
from django.http import HttpResponseRedirect
from Prosaist.models import Project, User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

#ToDO Refactor
def view_base(request, username, projectname, model, modelform, msg_success, msg_error):
    user_id = User.objects.get(username=username)
    project = Project.objects.get(name=projectname, owner_id=user_id)
    project_id = project.id
    form = modelform(initial={'project': project_id}, projectid=project_id)
    form.fields['project'].widget.attrs['readonly'] = True
    if request.method == 'POST':
        form = modelform(request.POST)
        if (form.is_valid()):
            try:
                category1 = int(request.POST.get('category1', ''))
                category2 = int(request.POST.get('category2', ''))
                id1 = min(category1,category2)
                id2 = max(category1,category2)
                try:
                    model.objects.get(project=project,category_1_id=id1, category_2_id=id2)
                    messages.add_message(request, messages.ERROR, msg_error)
                except:
                    if category1 != category2 and category1 != '' and category2 != '':
                        object = model(project=project, category_1_id=id1, category_2_id=id2)
                        object.save()
                        messages.add_message(request, messages.SUCCESS, msg_success)
                    else:
                        messages.add_message(request, messages.ERROR, msg_error)
            except ObjectDoesNotExist:
                messages.add_message(request, messages.ERROR, msg_error)
            return HttpResponseRedirect('.')
    return render(request, "inputform.html", {'form': form, 'username': username, 'projectname': projectname})
