from django.shortcuts import render


def view(request, username, projectname):
    return render(request, "base.html", {'username': username, 'projectname': projectname})
