from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^event/(?P<event_id>[0-9]+)$', views.event, name='event'),
	url(r'^project/(?P<project_id>[0-9]+)$', views.project, name='project'),
	url(r'^person/(?P<person_id>[0-9]+)$', views.person, name='person'),
	url(r'^company/(?P<company_id>[0-9]+)$', views.company, name='company'),
	url(r'^people$', views.people, name='people'),
	url(r'^companies$', views.companies, name='companies'),
	url(r'^trombinoscope$', views.trombinoscope, name='trombinoscope'),
	url(r'^autocomplete/', include('autocomplete_light.urls')),
]