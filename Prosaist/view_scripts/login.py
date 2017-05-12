from django.shortcuts import render
from django.http import HttpResponseRedirect
from Prosaist.view_scripts.forms.login import LoginForm


def view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if(form.is_valid()):
            return HttpResponseRedirect('..')
    else:
        form = LoginForm()
    return render(request, "userform.html", {'form' : form})
