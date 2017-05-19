from django.conf.urls import url

from Prosaist.views import index, login, logout, signup, entity

urlpatterns = [
     url(r'^$', index, name='index')
    ,url(r'^login/$', login, name='login')
    ,url(r'^logout/$', logout, name='logout')
    ,url(r'^signup/$', signup, name='signup')
    ,url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w.@+-]+)/entity/$', entity, name='entity')
    ,url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w.@+-]+)/status/$', signup, name='status')
    ,url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w.@+-]+)/category/$', signup, name='category')
    ,url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w.@+-]+)/event/$', signup, name='event')
    #,url(r'^user/<username>[\w.@+-]+/$', userprofile, name='userprofile')
    #,url(r'^user/<username>[\w.@+-]+/<projectname>[\w.@+-]+/$', project, name='project')
    ,

]