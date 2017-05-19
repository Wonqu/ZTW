from Prosaist.view_scripts import index as view_index
from Prosaist.view_scripts import login as view_login
from Prosaist.view_scripts import logout as view_logout
from Prosaist.view_scripts import signup as view_signup
from Prosaist.view_scripts import event as view_event
from Prosaist.view_scripts import entity as view_entity
from Prosaist.view_scripts import category as view_category


def index(request):
    return view_index.view(request)


def login(request):
    return view_login.view(request)


def logout(request):
    return view_logout.view(request)


def signup(request):
    return view_signup.view(request)


def entity(request, username, projectname):
    return view_entity.view(request, username, projectname)


def entity(request):
    return view_entity.view(request)


def event(request):
    return view_event.view(request)


def category(request):
    return view_category.view(request)

