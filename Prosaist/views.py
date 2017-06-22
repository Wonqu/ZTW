from Prosaist.view_scripts import index as view_index
from Prosaist.view_scripts import login as view_login
from Prosaist.view_scripts import logout as view_logout
from Prosaist.view_scripts import signup as view_signup
from Prosaist.view_scripts import input_single_event as view_event
from Prosaist.view_scripts import input_single_entity as view_entity
from Prosaist.view_scripts import input_single_category as view_category
from Prosaist.view_scripts import input_single_status as view_status
from Prosaist.view_scripts import input_category_conflict as view_category_conflict
from Prosaist.view_scripts import input_period as view_period
from Prosaist.view_scripts import input_affectedby as view_affectedby
from Prosaist.view_scripts import input_belongsto as view_belongsto
from Prosaist.view_scripts import input_entity_relation as view_entity_relation
from Prosaist.view_scripts import input_status_conflict as view_status_conflict
from Prosaist.view_scripts import display_entity as view_entities
from Prosaist.view_scripts import display_status as view_statuses
from Prosaist.view_scripts import display_category as view_categories
from Prosaist.view_scripts import display_event as view_events
from Prosaist.view_scripts import display_category_conflicts as view_dis_category_conflict
from Prosaist.view_scripts import display_period as view_dis_period
from Prosaist.view_scripts import display_affectedby as view_dis_affectedby
from Prosaist.view_scripts import display_belongsto as view_dis_belongsto
from Prosaist.view_scripts import display_entity_relation as view_dis_entity_relation
from Prosaist.view_scripts import display_status_conflicts as view_dis_status_conflict
from Prosaist.view_scripts import display_userprojects as view_userprojects
from Prosaist.view_scripts import display_project as view_project


def index(request):
    return view_index.view(request)


def login(request):
    return view_login.view(request)


def logout(request):
    return view_logout.view(request)


def signup(request):
    return view_signup.view(request)


def userprojects(request, username):
    return view_userprojects.view(request, username)


def project(request, username, projectname):
    return view_project.view(request, username, projectname)


def entity(request, username, projectname):
    return view_entity.view(request, username, projectname)


def event(request, username, projectname):
    return view_event.view(request, username, projectname)


def status(request, username, projectname):
    return view_status.view(request, username, projectname)


def category(request, username, projectname):
    return view_category.view(request, username, projectname)


def category_conflict(request, username, projectname):
    return view_category_conflict.view(request, username, projectname)


def period(request, username, projectname):
    return view_period.view(request, username, projectname)


def affectedby(request, username, projectname):
    return view_affectedby.view(request, username, projectname)


def belongsto(request, username, projectname):
    return view_belongsto.view(request, username, projectname)


def entity_relation(request, username, projectname):
    return view_entity_relation.view(request, username, projectname)


def status_conflict(request, username, projectname):
    return view_status_conflict.view(request, username, projectname)


def display_entity(request, username, projectname):
    return view_entities.view(request, username, projectname)


def display_status(request, username, projectname):
    return view_statuses.view(request, username, projectname)


def display_category(request, username, projectname):
    return view_categories.view(request, username, projectname)


def display_event(request, username, projectname):
    return view_events.view(request, username, projectname)


def display_category_conflicts(request, username, projectname):
    return view_dis_category_conflict.view(request, username, projectname)


def display_period(request, username, projectname):
    return view_dis_period.view(request, username, projectname)


def display_affected(request, username, projectname):
    return view_dis_affectedby.view(request, username, projectname)


def display_belongsto(request, username, projectname):
    return view_dis_belongsto.view(request, username, projectname)


def display_entity_relation(request, username, projectname):
    return view_dis_entity_relation.view(request, username, projectname)


def display_status_conflicts(request, username, projectname):
    return view_dis_status_conflict.view(request, username, projectname)