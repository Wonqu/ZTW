from django.shortcuts import render
from django.http import HttpResponseRedirect
from Prosaist.models import Project, User, Period, AffectedBy, BelongsTo, Category_Conflict, Status_Conflict,\
    Entity_Relation
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from Prosaist.text.messages import message_affectedBy_conflict, message_belongsTo_conflict

#ToDO Refactor
def view_base(request, username, projectname, model, modelform, msg_success, msg_error):
    if request.user.is_authenticated:
        user_id = User.objects.get(username=username)
        project = Project.objects.get(name=projectname, owner_id=user_id)
        project_id = project.id
        form = modelform(initial={'project': project_id}, projectid=project_id)
        form.fields['project'].widget.attrs['readonly'] = True
        if request.method == 'POST':
            form = modelform(request.POST)
            if (form.is_valid()):
                try:
                    if model == Category_Conflict:
                        category1 = int(request.POST.get('category1', ''))
                        category2 = int(request.POST.get('category2', ''))
                        id1 = min(category1, category2)
                        id2 = max(category1, category2)
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
                    elif model == AffectedBy:
                        entity = int(request.POST.get('entity', ''))
                        period = int(request.POST.get('period', ''))
                        status = int(request.POST.get('status', ''))
                        try:
                            model.objects.get(project=project, entity_id=entity, period_id=period, status_id=status)
                            messages.add_message(request, messages.ERROR, msg_error)
                        except:
                            conflict1 = Status_Conflict.objects.filter(status_1_id=status)
                            conflict2 = Status_Conflict.objects.filter(status_2_id=status)
                            isConflict = False
                            for n in conflict1:
                                if model.objects.filter(project=project, entity_id=entity, period_id=period,
                                                      status_id=n.status_2_id).exists():
                                    messages.add_message(request, messages.ERROR, message_affectedBy_conflict)
                                    isConflict = True
                            for n in conflict2:
                                if model.objects.filter(project=project, entity_id=entity, period_id=period,
                                                      status_id=n.status_1_id).exists():
                                    messages.add_message(request, messages.ERROR, message_affectedBy_conflict)
                                    isConflict = True
                            if not isConflict:
                                object = model(project=project, entity_id=entity, period_id=period, status_id=status)
                                object.save()
                                messages.add_message(request, messages.SUCCESS, msg_success)
                            else:
                                messages.add_message(request, messages.ERROR, msg_error)
                    elif model == Period:
                        event1 = int(request.POST.get('event1', ''))
                        event2 = int(request.POST.get('event2', ''))
                        name = (request.POST.get('name', ''))
                        try:
                            model.objects.get(project=project, event_start_id=event1, event_end_id=event2, name=name)
                            messages.add_message(request, messages.ERROR, msg_error)
                        except:
                            if event1 != '' and event2 != '' and name != '':  #ToDo Dodać warunek kolejności wydarzeń
                                object = model(project=project, event_start_id=event1, event_end_id=event2, name=name)
                                object.save()
                                messages.add_message(request, messages.SUCCESS, msg_success)
                            else:
                                messages.add_message(request, messages.ERROR, msg_error)
                    elif model == BelongsTo:
                        entity = int(request.POST.get('entity', ''))
                        category = int(request.POST.get('category', ''))
                        try:
                            model.objects.get(project=project, entity_id=entity, category_id=category)
                            messages.add_message(request, messages.ERROR, msg_error)
                        except:
                            conflict1 = Category_Conflict.objects.filter(category_1_id=category)
                            conflict2 = Category_Conflict.objects.filter(category_2_id=category)
                            isConflict = False
                            for n in conflict1:
                                if model.objects.filter(project=project, entity_id=entity,
                                                        category_id=n.category_2_id).exists():
                                    messages.add_message(request, messages.ERROR, message_belongsTo_conflict)
                                    isConflict = True
                            for n in conflict2:
                                if model.objects.filter(project=project, entity_id=entity,
                                                        category_id=n.category_1_id).exists():
                                    messages.add_message(request, messages.ERROR, message_belongsTo_conflict)
                                    isConflict = True
                            if not isConflict:
                                object = model(project=project, entity_id=entity, category_id=category)
                                object.save()
                                messages.add_message(request, messages.SUCCESS, msg_success)
                            else:
                                messages.add_message(request, messages.ERROR, msg_error)
                    elif model == Status_Conflict:
                        category1 = int(request.POST.get('status1', ''))
                        category2 = int(request.POST.get('status2', ''))
                        id1 = min(category1, category2)
                        id2 = max(category1, category2)
                        try:
                            model.objects.get(project=project,status_1_id=id1, status_2_id=id2)
                            messages.add_message(request, messages.ERROR, msg_error)
                        except:
                            if category1 != category2 and category1 != '' and category2 != '':
                                object = model(project=project, status_1_id=id1, status_2_id=id2)
                                object.save()
                                messages.add_message(request, messages.SUCCESS, msg_success)
                            else:
                                messages.add_message(request, messages.ERROR, msg_error)
                    elif model == Entity_Relation:
                        category1 = int(request.POST.get('entity1', ''))
                        category2 = int(request.POST.get('entity2', ''))
                        period = int(request.POST.get('period', ''))
                        id1 = min(category1, category2)
                        id2 = max(category1, category2)
                        name = request.POST.get('name','')
                        try:
                            model.objects.get(name=name, project=project, entity_1_id=id1, entity_2_id=id2, period_id=period)
                            messages.add_message(request, messages.ERROR, msg_error)
                        except:
                            if category1 != category2 and category1 != '' and category2 != '' and period != '':
                                object = model(name=name,project=project, entity_1_id=id1, entity_2_id=id2, period_id=period)
                                object.save()
                                messages.add_message(request, messages.SUCCESS, msg_success)
                            else:
                                messages.add_message(request, messages.ERROR, msg_error)

                except ObjectDoesNotExist:
                    messages.add_message(request, messages.ERROR, msg_error)
                return HttpResponseRedirect('.')
        return render(request, "inputform.html", {'form': form, 'username': username, 'projectname': projectname})
    else:
        return HttpResponseRedirect('/prosaist/')
