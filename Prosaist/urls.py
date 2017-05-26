from django.conf.urls import url

from Prosaist.views import index, login, logout, signup, event, entity, category, category_conflict, period, status, display_entity, \
    display_status, display_category, display_event, display_category_conflicts

urlpatterns = [
     url(r'^$', index, name='index')
    ,url(r'^login/$', login, name='login')
    ,url(r'^logout/$', logout, name='logout')
    ,url(r'^signup/$', signup, name='signup')
    ,url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w.@+-]+)/entity/$', entity, name='entity')
    ,url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w.@+-]+)/status/$', status, name='status')
    ,url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w.@+-]+)/category/$', category, name='category')
    ,url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w.@+-]+)/event/$', event, name='event')
    ,url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w.@+-]+)/category_conflict/$', category_conflict, name='category_conflict')
    ,url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w.@+-]+)/period/$', period, name='period')
    ,url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w.@+-]+)/entities/$', display_entity, name='display_entity')
    ,url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w.@+-]+)/statuses/$', display_status, name='display_status')
    ,url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w.@+-]+)/categories/$', display_category, name='display_category')
    ,url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w.@+-]+)/events/$', display_event, name='display_event')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w.@+-]+)/category_conflicts/$', display_category_conflicts, name='display_category_conflicts')
    #,url(r'^user/<username>[\w.@+-]+/$', userprofile, name='userprofile')
    #,url(r'^user/<username>[\w.@+-]+/<projectname>[\w.@+-]+/$', project, name='project')
    ,

]