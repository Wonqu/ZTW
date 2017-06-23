from django.shortcuts import render
from Prosaist.models import Project, User, AffectedBy, BelongsTo, Category_Conflict, Entity_Relation, Period, Status_Conflict
from django.http import HttpResponseRedirect
from Prosaist.view_scripts.delete import links


def dellink(model):
    return 'delete' + links[model._meta.object_name]


def view(request, username, projectname, model):
    if request.user.is_authenticated:
        user_id = User.objects.get(username=username)
        project = Project.objects.get(name=projectname, owner_id=user_id)
        project_id = project.id
        objects = model.objects.filter(project_id=project_id)
        if model == AffectedBy:
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                                                        'model': 'aff', 'dellink': dellink(model)})
        elif model == BelongsTo:
            return render(request, "displaydata.html", {'data': objects.order_by('category_id'), 'username': username, 'projectname': projectname,
                                                        'model': 'bel', 'dellink': dellink(model)})
        elif model == Category_Conflict:
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                                                        'model': 'c_c', 'dellink': dellink(model)})
        elif model == Entity_Relation:
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                                                        'model': 'e_r', 'dellink': dellink(model)})
        elif model == Period:
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                                                        'model': 'per', 'dellink': dellink(model)})
        elif model == Status_Conflict:
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                                                        'model': 's_c', 'dellink': dellink(model)})
        else:
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                                                        'model': 'single', 'dellink': dellink(model)})
    else:
        return HttpResponseRedirect('/prosaist/')
