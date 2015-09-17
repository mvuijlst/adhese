from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^event/(?P<event_id>[0-9]+)$', views.event, name='event'),
	url(r'^autocomplete/', include('autocomplete_light.urls')),
]