from Prosaist.view_scripts.forms.status_conflict import StatusConflictCreateForm as modelform
from Prosaist.models import Status_Conflict as model
from Prosaist.text.messages import message_statusConflict_success as msg_success
from Prosaist.text.messages import message_statusConflict_error as msg_error

from Prosaist.view_scripts.input_concat_base import view_base as view_input


def view(request, username, projectname):
    return view_input(request=request, username=username, projectname=projectname, model=model,
                      modelform=modelform, msg_success=msg_success,
                      msg_error=msg_error)
