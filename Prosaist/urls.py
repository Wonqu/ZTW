from django.conf.urls import url

from Prosaist.views import index, login, logout, signup, event, entity, category, status, display_entity, \
    display_status, display_category, display_event

urlpatterns = [
     url(r'^$', index, name='index')
    ,url(r'^login/$', login, name='login')
    ,url(r'^logout/$', logout, name='logout')
    ,url(r'^signup/$', signup, name='signup')
    ,url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w.@+-]+)/entity/$', entity, name='entity')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w.@+-]+)/status/$', status, name='status')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w.@+-]+)/category/$', category, name='category')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w.@+-]+)/event/$', event, name='event')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w.@+-]+)/entities/$', display_entity, name='display_entity')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w.@+-]+)/statuses/$', display_status, name='display_status')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w.@+-]+)/categories/$', display_category,
          name='display_category')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w.@+-]+)/events/$', display_event, name='display_event')
    #,url(r'^user/<username>[\w.@+-]+/$', userprofile, name='userprofile')
    #,url(r'^user/<username>[\w.@+-]+/<projectname>[\w.@+-]+/$', project, name='project')
    ,

]