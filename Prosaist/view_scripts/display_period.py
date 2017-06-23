from Prosaist.view_scripts.display_base import view as view_base, show as filter_base
from Prosaist.models import Period


def view(request, username, projectname):
    return view_base(request=request, username=username, projectname=projectname, model=Period)


def show(request, username, projectname, object, attrib):
    return filter_base(request=request, username=username, projectname=projectname, model=Period, object=object,
                       attrib=attrib)
