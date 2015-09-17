from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
from datetime import datetime, timedelta

from .models import *

def index(request):
	recenteventlist = Event.objects.filter(
		datetime__lte=datetime.today()
		).order_by('-datetime')[:10]
		
	upcomingeventlist = Event.objects.filter(
		datetime__gte=datetime.today()
		).order_by('datetime')[:10]

	projectlist = Project.objects.all().order_by('name')
		
	context = {
		'recenteventlist': recenteventlist,
		'upcomingeventlist': upcomingeventlist,
		'projectlist': projectlist,
	}
	
	return render(request, 'crm/index.html', context)

def event(request, event_id):
	try:
		event=Event.objects.get(pk=event_id)
	except Event.DoesNotExist:
		raise Http404("Event does not exist. I think.")
		
	context = {
		'event': event
	}
	
	return render(request, 'crm/event.html', context)