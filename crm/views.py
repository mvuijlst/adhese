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

	projectlist = Project.objects.all().filter(active=True).order_by('name')
	
	todolist = Note.objects.all().filter(notetype__name__startswith='todo').order_by('actiondate')
		
	context = {
		'recenteventlist': recenteventlist,
		'upcomingeventlist': upcomingeventlist,
		'projectlist': projectlist,
		'todolist': todolist,
	}
	
	return render(request, 'crm/index.html', context)

def event(request, event_id):
	try:
		event=Event.objects.get(pk=event_id)
	except Event.DoesNotExist:
		raise Http404("Event does not exist. I think.")
	
	personlist=Person.objects.raw("""
		SELECT p.id, p.firstname, p.lastname, c.id companyid, c.name companyname 
		FROM crm_person p
			INNER JOIN crm_event_persons ep ON ep.person_id=p.id 
			left outer join crm_company c ON p.company_id=c.id
		WHERE  ep.event_id={0}
		ORDER BY c.name, p.lastname
		""".format(event_id))
	notes = Note.objects.filter(event=event_id).order_by('-datetime')
		
	context = {
		'event': event,
		'personlist': personlist,
		'notes': notes,
		'now': datetime.now(),
	}
	
	return render(request, 'crm/event.html', context)

def project(request, project_id):
	try:
		project=Project.objects.get(pk=project_id)
	except Project.DoesNotExist:
		raise Http404("No such project, far as I know.")
	
	context = {
		'project': project,	
	}
	
	return render(request, 'crm/project.html', context)

def person(request, person_id):
	try:
		person=Person.objects.get(pk=person_id)
	except Person.DoesNotExist:
		raise Http404("Bleep bloop. Person unknown.")
	
	contacts = Contact.objects.filter(person=person_id).filter(valid=True).order_by('contacttype__id')
	notes = Note.objects.filter(person=person_id).order_by('-datetime')

	context = {
		'person': person,
		'contacts': contacts,
		'notes': notes,
	}
	
	return render(request, 'crm/person.html', context)

def company(request, company_id):
	try:
		company=Company.objects.get(pk=company_id)
	except Company.DoesNotExist:
		raise Http404("?SN ERR. #company# NT FND.")
		
	contacts = Contact.objects.filter(company=company_id).filter(valid=True).order_by('contacttype__id')
	notes = Note.objects.filter(company=company_id).order_by('-datetime')
	personlist = Person.objects.filter(company=company_id).order_by('lastname')
	
	context = {
		'company': company,
		'contacts': contacts,
		'personlist': personlist,
		'notes': notes,
	}
	
	return render(request, 'crm/company.html', context)

def companies(request):
	companylist = Company.objects.raw("""
		SELECT id, name, upper(left(name,1)) initial
		FROM crm_company
		ORDER BY name
	""")
	
	context = {
		'companylist': companylist,
	}
	
	return render(request, 'crm/companies.html', context)
	
def people(request):
	personlist=Person.objects.raw("""
		SELECT p.id, p.firstname, upper(left(p.lastname,1)) initial, p.lastname, c.id companyid, c.name companyname 
		FROM crm_person p
			LEFT OUTER JOIN crm_company c ON p.company_id=c.id
		ORDER BY p.lastname, p.firstname
		""")
	
	context = {
		'personlist': personlist,
	}
	
	return render(request, 'crm/people.html', context)

def trombinoscope(request):
	photolist=Person.objects.all().order_by('?')
	
	context = { 
		'photolist': photolist 
	}
	return render(request, 'crm/trombinoscope.html', context)