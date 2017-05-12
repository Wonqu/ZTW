from django.conf.urls import url

from Prosaist.views import index, login, logout, signup, event, entity, category

urlpatterns = [
     url(r'^$', index, name='index')
    ,url(r'^login/$', login, name='login')
    ,url(r'^logout/$', logout, name='logout')
    ,url(r'^signup/$', signup, name='signup')
    ,url(r'^entity/$', entity, name='entity')
    ,url(r'^status/$', entity, name='status')
    ,url(r'^category/$', category, name='category')
    ,url(r'^event/$', event, name='event')

]