from django.conf.urls import url

from Prosaist.views import *

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
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/category_conflicts/$', display_category_conflicts,
          name='display_category_conflicts')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/periods/$', display_period,
          name='display_period')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/affecteds/$', display_affected,
          name='display_affectedby')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/belongstos/$', display_belongsto,
          name='display_belongsto')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/entity_relations/$', display_entity_relation,
          name='display_entity_relation')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/status_conflicts/$', display_status_conflicts,
          name='display_status_conflict')

    # Delete
    ,
    url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/entities/delete/(?P<id>[\w\s.@+-]+)$', delete_entity,
        name='delete_entity')
    ,
    url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/statuses/delete/(?P<id>[\w\s.@+-]+)$', delete_status,
        name='delete_status')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/categories/delete/(?P<id>[\w\s.@+-]+)$',
          delete_category, name='delete_category')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/events/delete/(?P<id>[\w\s.@+-]+)$', delete_event,
          name='delete_event')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/category_conflicts/delete/(?P<id>[\w\s.@+-]+)$',
          delete_cat_conf, name='delete_cat_conf')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/periods/delete/(?P<id>[\w\s.@+-]+)$', delete_period,
          name='delete_period')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/affecteds/delete/(?P<id>[\w\s.@+-]+)$',
          delete_affected, name='delete_affected')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/belongstos/delete/(?P<id>[\w\s.@+-]+)$',
          delete_belongsto, name='delete_belongsto')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/entity_relations/delete/(?P<id>[\w\s.@+-]+)$',
          delete_entity_relation, name='delete_entity_relation')
    , url(r'^u/(?P<username>[\w.@+-]+)/(?P<projectname>[\w\s.@+-]+)/status_conflicts/delete/(?P<id>[\w\s.@+-]+)$',
          delete_status_conflict, name='delete_status_conflict')

]