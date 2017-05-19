from django.shortcuts import render
from django.http import HttpResponseRedirect
from Prosaist.view_scripts.forms.signup import UserCreateForm as SignupForm
from django.contrib.auth import authenticate, login
from django.contrib.sessions.backends.db import SessionStore


def view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if(form.is_valid()):
            form.save()
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
            s = SessionStore(session_key=request.session.id)
            s['username'] = form.cleaned_data["username"]
            login(request, user)
            return HttpResponseRedirect('..')
    else:
        form = SignupForm()
    return render(request, "userform.html", {'form' : form})