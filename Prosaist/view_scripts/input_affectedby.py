from Prosaist.view_scripts.forms.affectedby import AffectedByCreateForm as modelform
from Prosaist.models import AffectedBy as model
from Prosaist.models import User, Project, Status_Conflict
from Prosaist.text.messages import message_affectedBy_success as msg_success
from Prosaist.text.messages import message_affectedBy_error as msg_error

from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

from Prosaist.view_scripts.input_concat_base import view_base as view_input


def view(request, username, projectname):

    return  view_input(request=request, username=username, projectname=projectname, model=model,
                      modelform=modelform, msg_success=msg_success,
                      msg_error=msg_error)