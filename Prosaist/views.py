from Prosaist.view_scripts import index as view_index
from Prosaist.view_scripts import login as view_login
from Prosaist.view_scripts import logout as view_logout
from Prosaist.view_scripts import signup as view_signup
from Prosaist.view_scripts import entity as view_entity


def index(request):
    return view_index.view(request)


def login(request):
    return view_login.view(request)


def logout(request):
    return view_logout.view(request)


def signup(request):
    return view_signup.view(request)

def entity(request):
    return view_entity.view(request)