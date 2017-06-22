from django.shortcuts import render
from django.http import HttpResponseRedirect


def view(request, username, projectname):
    if request.user.is_authenticated:
        return render(request, "base.html", {'username': username, 'projectname': projectname})
    else:
        return HttpResponseRedirect('/prosaist/')

