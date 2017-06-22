from django.shortcuts import render
from Prosaist.models import Project, User, AffectedBy, BelongsTo, Category_Conflict, Entity_Relation, Period, Status_Conflict
from django.http import HttpResponseRedirect


def view(request, username, projectname, model):
    if request.user.is_authenticated:
        user_id = User.objects.get(username=username)
        project = Project.objects.get(name=projectname, owner_id=user_id)
        project_id = project.id
        objects = model.objects.filter(project_id=project_id)
        if model == AffectedBy:
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                                                        'model': 'aff'})
        elif model == BelongsTo:
            return render(request, "displaydata.html", {'data': objects.order_by('category_id'), 'username': username, 'projectname': projectname,
                                                        'model': 'bel'})
        elif model == Category_Conflict:
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                                                        'model': 'c_c'})
        elif model == Entity_Relation:
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                                                        'model': 'e_r'})
        elif model == Period:
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                                                        'model': 'per'})
        elif model == Status_Conflict:
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                                                        'model': 's_c'})
        else:
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                                                        'model': 'single'})
    else:
        return HttpResponseRedirect('/prosaist/')
