from django.contrib import admin
from django import forms
import autocomplete_light

from .models import *

class ContactInline(admin.TabularInline):
	model=Contact
	extra=0

class PersonForm(autocomplete_light.ModelForm):
	class Meta:
		model=Person
		autocomplete_fields=('company')
		exclude=['']
		
class PersonAdmin(admin.ModelAdmin):
	form=PersonForm
	inlines=[ContactInline]
	list_display = ('firstname', 'lastname', 'company')
	search_fields = ['firstname', 'lastname', 'company__name'] 

admin.site.register(Person,PersonAdmin)

class EventForm(autocomplete_light.ModelForm):
	class Meta:
		model=Event
		autocomplete_fields=('location', 'project', 'companies', 'persons')
		exclude=['']
		
class EventAdmin(admin.ModelAdmin):
	form=EventForm
	list_display = ('datetime', 'eventtype', 'project')
	list_filter = ['project']
	search_fields = ['person__firstname', 'person__lastname', 'memo']

admin.site.register(Event, EventAdmin)

admin.site.register(Eventtype)
admin.site.register(Companytype)
admin.site.register(Contact)
admin.site.register(Contacttype)
admin.site.register(Project)
admin.site.register(Location)
admin.site.register(Relation)

class CompanyForm(autocomplete_light.ModelForm):
	class Meta:
		model=Company
		autocomplete_fields=('parentcompany')
		exclude=['']
		
class CompanyAdmin(admin.ModelAdmin):
	form=CompanyForm

admin.site.register(Company,CompanyAdmin)