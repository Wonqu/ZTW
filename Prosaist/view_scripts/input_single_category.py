from Prosaist.view_scripts.forms.category import CategoryCreateForm as modelform
from Prosaist.models import Category as model
from Prosaist.text.messages import message_category_success as msg_success
from Prosaist.text.messages import message_category_error as msg_error

from Prosaist.view_scripts.input_single_base import view_base as view_input


def view(request, username, projectname):
    return view_input(request=request, username=username, projectname=projectname, model=model,
                      modelform=modelform, msg_success=msg_success,
                      msg_error=msg_error)
