from Prosaist.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse

links = {
    'Entity': '_entity'
    , 'Status': '_status'
    , 'Category': '_category'
    , 'Event': '_event'
    , 'Category_Conflict': '_cat_conf'
    , 'Period': '_period'
    , 'AffectedBy': '_affectedby'
    , 'BelongsTo': '_belongsto'
    , 'Entity_Relation': '_entity_relation'
    , 'Status_Conflict': '_status_conflict'
}


def delete_entity(request, username, projectname, id):
    return __auth_delete(Entity, request, username, projectname, id)


def delete_status(request, username, projectname, id):
    return __auth_delete(Status, request, username, projectname, id)


def delete_category(request, username, projectname, id):
    return __auth_delete(Category, request, username, projectname, id)


def delete_event(request, username, projectname, id):
    return __auth_delete(Event, request, username, projectname, id)


def delete_cat_conf(request, username, projectname, id):
    return __auth_delete(Category_Conflict, request, username, projectname, id)


def delete_period(request, username, projectname, id):
    return __auth_delete(Period, request, username, projectname, id)


def delete_affected(request, username, projectname, id):
    return __auth_delete(AffectedBy, request, username, projectname, id)


def delete_belongsto(request, username, projectname, id):
    return __auth_delete(BelongsTo, request, username, projectname, id)


def delete_entity_relation(request, username, projectname, id):
    return __auth_delete(Entity_Relation, request, username, projectname, id)


def delete_status_conflict(request, username, projectname, id):
    return __auth_delete(Status_Conflict, request, username, projectname, id)


def __auth_delete(model, request, username, projectname, id):
    if request.user.is_authenticated and request.user.username == username:
        __delete_object(model, id)
        return __redirect(model, username, projectname)


def __redirect(model, username, projectname):
    return HttpResponseRedirect(reverse(__display(model), args=[username, projectname]))


def __display(model):
    return 'display' + links[model._meta.object_name]


def __delete_object(model, id):
    model.objects.get(id=id).delete()
