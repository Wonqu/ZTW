from django.shortcuts import render
from django.http import HttpResponseRedirect
from Prosaist.view_scripts.forms.signup import UserCreateForm as SignupForm
from django.contrib.auth import authenticate, login


def view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if(form.is_valid()):
            form.save()
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
            if user is not None:
                login(request, user)
            return HttpResponseRedirect('..')
    else:
        form = SignupForm()
    return render(request, "userform.html", {'form' : form})