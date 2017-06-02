from Prosaist.view_scripts.forms.entity_relation import EntityRelationCreateForm as modelform
from Prosaist.models import Entity_Relation as model
from Prosaist.text.messages import message_entityRelation_success as msg_success
from Prosaist.text.messages import message_entityRelation_error as msg_error

from Prosaist.view_scripts.input_concat_base import view_base as view_input


def view(request, username, projectname):
    return view_input(request=request, username=username, projectname=projectname, model=model,
                      modelform=modelform, msg_success=msg_success,
                      msg_error=msg_error)
