from django.conf.urls import url

from Prosaist.views import index, login, logout, signup, entity

urlpatterns = [
     url(r'^$', index, name='index')
    ,url(r'^login/$', login, name='login')
    ,url(r'^logout/$', logout, name='logout')
    ,url(r'^signup/$', signup, name='signup')
    ,url(r'^entity/$', entity, name='entity')
    ,url(r'^status/$', signup, name='status')
    ,url(r'^category/$', signup, name='category')
    ,url(r'^event/$', signup, name='event')

]