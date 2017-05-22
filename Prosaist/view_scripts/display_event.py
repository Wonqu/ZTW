from Prosaist.view_scripts.display_base import view as view_base
from Prosaist.models import Event


def view(request, username, projectname):
    return view_base(request=request, username=username, projectname=projectname, model=Event)
