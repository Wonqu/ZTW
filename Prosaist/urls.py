from django.conf.urls import url

from Prosaist.views import index, login, logout, signup, event, entity, category, category_conflict, period, affectedby, \
    belongsto, status_conflict, entity_relation, status, display_entity,display_status, display_category, display_event, \
    display_category_conflicts, display_affected, display_belongsto, display_entity_relation, display_period,\
    display_status_conflicts, userprojects, project

urlpatterns = [
     url(r'^$', index, name='index')
    , url(r'^login/$', login, name='login')
    , url(r'^logout/$', logout, name='logout')
    , url(r'^signup/$', signup, name='signup')
    # User
    , url(r'^u/(?P<username>[\w.@+-]+)/$', userprojects, name='userprojects')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/$', project, name='project')
    #Single input
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/entity/$', entity, name='entity')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/status/$', status, name='status')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/category/$', category, name='category')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/event/$', event, name='event')
    #Concat input
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/category_conflict/$', category_conflict,
          name='category_conflict')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/period/$', period, name='period')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/entity_relation/$', entity_relation,
          name='entity_relation')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/affectedby/$', affectedby, name='affectedby')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/belongsto/$', belongsto, name='belongsto')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/status_conflict/$', status_conflict,
          name='status_conflict')

    #Display
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/entities/$', display_entity, name='display_entity')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/statuses/$', display_status, name='display_status')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/categories/$', display_category,
          name='display_category')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/events/$', display_event, name='display_event')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/dis_category_conflicts/$', display_category_conflicts,
          name='display_category_conflicts')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/dis_period/$', display_period,
          name='display_period')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/dis_affected/$', display_affected,
          name='display_affectedby')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/dis_belongsto/$', display_belongsto,
          name='display_belongsto')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/dis_entity_relation/$', display_entity_relation,
          name='display_entity_relation')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/dis_status_conflict/$', display_status_conflicts,
          name='display_status_conflict')

]