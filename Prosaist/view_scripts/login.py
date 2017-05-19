from django.shortcuts import render
from django.http import HttpResponseRedirect
from Prosaist.view_scripts.forms.login import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from Prosaist.text import messages as msg

def view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if(form.is_valid()):
            try:
                user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
                if user is not None:
                    request.session['username'] = form.cleaned_data["username"]
                    login(request, user)
                    messages.add_message(request, messages.SUCCESS, msg.message_login_success)
            except KeyError:
                messages.add_message(request, messages.SUCCESS, msg.message_login_error)
            return HttpResponseRedirect('..')
    else:
        form = LoginForm()
    return render(request, "userform.html", {'form' : form})
