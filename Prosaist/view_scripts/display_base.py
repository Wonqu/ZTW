from django.shortcuts import render
from Prosaist.models import *
from django.http import HttpResponseRedirect
from django.db.models import Q
from Prosaist.view_scripts.delete import links


def dellink(model):
    return 'delete' + links[model._meta.object_name]


def view(request, username, projectname, model):
    if request.user.is_authenticated:
        user_id = User.objects.get(username=username)
        project = Project.objects.get(name=projectname, owner_id=user_id)
        project_id = project.id
        objects = model.objects.filter(project_id=project_id)
        link = dellink(model)
        if model == AffectedBy:
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                           'model': 'entities', 'elem': 'All', 'dellink' : link})
        elif model == Status:
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                           'model': 'status', 'elem': 'All', 'dellink' : link})
        elif model == Category:
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                           'model': 'categories', 'elem': 'All', 'dellink' : link})
        elif model == Event:
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                           'model': 'events', 'elem': 'All', 'dellink' : link})
        elif model == AffectedBy:
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                                                        'model': 'affected by', 'elem': 'All', 'dellink' : link})
        elif model == BelongsTo:
            return render(request, "displaydata.html", {'data': objects.order_by('category_id'), 'username': username, 'projectname': projectname,
                                                        'model': 'belongs to', 'elem': 'All', 'dellink' : link})
        elif model == Category_Conflict:
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                                                        'model': 'category conflicts', 'elem': 'All', 'dellink' : link})
        elif model == Entity_Relation:
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                                                        'model': 'entity relations', 'elem': 'All', 'dellink' : link})
        elif model == Period:
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                                                        'model': 'periods', 'elem': 'All', 'dellink' : link})
        elif model == Status_Conflict:
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                                                        'model': 'status conflicts', 'elem': 'All', 'dellink' : link})
    else:
        return HttpResponseRedirect('/prosaist/')


def show(request, username, projectname, model, object, attrib):
    if request.user.is_authenticated:
        user_id = User.objects.get(username=username)
        project = Project.objects.get(name=projectname, owner_id=user_id)
        project_id = project.id
        objects = model.objects.filter(project_id=project_id)
        link = dellink(model)
        if model == AffectedBy:
            if attrib == 'Entity object':
                objects = model.objects.filter(project_id=project_id, entity_id=object)
                elem = Entity.objects.get(project_id=project_id, id=object).name
            elif attrib == 'Period object':
                objects = model.objects.filter(project_id=project_id, period_id=object)
                elem = Period.objects.get(project_id=project_id, id=object).name
            elif attrib == 'Status object':
                objects = model.objects.filter(project_id=project_id, status_id=object)
                elem = Status.objects.get(project_id=project_id, id=object).name
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                                                        'model': 'affected by', 'elem': elem, 'dellink' : link})
        elif model == BelongsTo:
            if attrib == 'Entity object':
                objects = model.objects.filter(project_id=project_id, entity_id=object)
                elem = Entity.objects.get(project_id=project_id, id=object).name
            elif attrib == 'Category object':
                objects = model.objects.filter(project_id=project_id, category_id=object)
                elem = Category.objects.get(project_id=project_id, id=object).name
            return render(request, "displaydata.html", {'data': objects.order_by('category_id'), 'username': username,
                                                        'projectname': projectname, 'model': 'belongs to', 'elem': elem, 'dellink' : link})
        elif model == Category_Conflict:
            if attrib == 'Category object':
                objects = model.objects.filter(Q(project_id=project_id, category_1_id=object) | Q(project_id=project_id,
                                                                                                  category_2_id=object))
                elem = Category.objects.get(project_id=project_id, id=object).name
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                                                        'model': 'category conflicts', 'elem': elem, 'dellink' : link})
        elif model == Entity_Relation:
            if attrib == 'Entity object':
                objects = model.objects.filter(Q(project_id=project_id, entity_1_id=object) | Q(project_id=project_id,
                                                                                                  entity_2_id=object))
                elem = Entity.objects.get(project_id=project_id, id=object).name
            elif attrib == 'Period object':
                objects = model.objects.filter(project_id=project_id, period_id=object)
                elem = Period.objects.get(project_id=project_id, id=object).name
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                                                        'model': 'entity relations', 'elem': elem, 'dellink' : link})
        elif model == Period:
            if attrib == 'Event object':
                objects = model.objects.filter(Q(project_id=project_id, event_start_id=object) | Q(project_id=project_id,
                                                                                                  event_end_id=object))
                elem = Event.objects.get(project_id=project_id, id=object).name
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                                                        'model': 'periods', 'elem': elem, 'dellink' : link})
        elif model == Status_Conflict:
            if attrib == 'Status object':
                objects = model.objects.filter(Q(project_id=project_id, status_1_id=object) | Q(project_id=project_id,
                                                                                                  status_2_id=object))
                elem = Status.objects.get(project_id=project_id, id=object).name
            return render(request, "displaydata.html", {'data': objects, 'username': username, 'projectname': projectname,
                                                        'model': 'status conflicts', 'elem': elem, 'dellink' : link})
    else:
        return HttpResponseRedirect('/prosaist/')
