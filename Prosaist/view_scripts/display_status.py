from Prosaist.view_scripts.display_base import view as view_base
from Prosaist.models import Status


def view(request, username, projectname):
    return view_base(request=request, username=username, projectname=projectname, model=Status)
