from django.conf.urls import url

from Prosaist.views import index, login, logout, signup

urlpatterns = [
     url(r'^$', index, name='index')
    ,url(r'^login/$', login, name='login')
    ,url(r'^logout/$', logout, name='logout')
    ,url(r'^signup/$', signup, name='signup')

]