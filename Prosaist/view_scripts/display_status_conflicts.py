from Prosaist.view_scripts.display_base import view as view_base, show as filter_base
from Prosaist.models import Status_Conflict


def view(request, username, projectname):
    return view_base(request=request, username=username, projectname=projectname, model=Status_Conflict)


def show(request, username, projectname, object, attrib):
    return filter_base(request=request, username=username, projectname=projectname, model=Status_Conflict,
                       object=object,
                       attrib=attrib)
