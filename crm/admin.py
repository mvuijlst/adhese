# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
import autocomplete_light

from .models import *

class PersonContactInline(admin.TabularInline):
	model=Contact
	exclude=('company',)
	extra=0

class CompanyContactInline(admin.TabularInline):
	model=Contact
	exclude=('person',)
	extra=0

class PersonNoteInline(admin.StackedInline):
	model=Note
	def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
		field = super(PersonNoteInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
		if db_field.name == 'actionperson':
			field.queryset = field.queryset.filter(company__name__exact = 'Adhese')  
		return field
	fk_name='person'
	exclude=('company','event','project',)
	readonly_fields=('datetime',)
	extra=0

class CompanyNoteInline(admin.StackedInline):
	model=Note
	def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
		field = super(CompanyNoteInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
		if db_field.name == 'actionperson':
			field.queryset = field.queryset.filter(company__name__exact = 'Adhese')  
		return field
	exclude=('person','event','project',)
	readonly_fields=('datetime',)
	extra=0
	
class EventNoteInline(admin.StackedInline):
	model=Note
	def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
		field = super(EventNoteInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
		if db_field.name == 'actionperson':
			field.queryset = field.queryset.filter(company__name__exact = 'Adhese')  
		return field
	exclude=('person','company','project',)
	readonly_fields=('datetime',)
	extra=0
	
class ProjectNoteInline(admin.StackedInline):
	model=Note
	def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
		field = super(ProjectNoteInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
		if db_field.name == 'actionperson':
			field.queryset = field.queryset.filter(company__name__exact = 'Adhese')  
		return field
	exclude=('person','company','event',)
	readonly_fields=('datetime',)
	extra=0
	
class PersonForm(autocomplete_light.ModelForm):
	class Meta:
		model=Person
		autocomplete_fields=('company')
		exclude=['']
		
class PersonAdmin(admin.ModelAdmin):
	form=PersonForm
	inlines=[PersonContactInline, PersonNoteInline]
	list_display = ('firstname', 'lastname', 'company')
	list_display_links = ('firstname', 'lastname')
	search_fields = ['firstname', 'lastname', 'company__name'] 

admin.site.register(Person,PersonAdmin)

class EventForm(autocomplete_light.ModelForm):
	class Meta:
		model=Event
		autocomplete_fields=('location', 'project', 'persons')
		exclude=['']
		
class EventAdmin(admin.ModelAdmin):
	form=EventForm
	inlines=[EventNoteInline]
	list_display = ('datetime', 'eventtype', 'project')
	list_filter = ['project']
	search_fields = ['person__firstname', 'person__lastname', 'memo']

admin.site.register(Event, EventAdmin)
	
class ProjectAdmin(admin.ModelAdmin):
	inlines=[ProjectNoteInline]
	
admin.site.register(Project, ProjectAdmin)
	
class CompanyForm(autocomplete_light.ModelForm):
	class Meta:
		model=Company
		autocomplete_fields=('parentcompany')
		exclude=['']
		
class CompanyAdmin(admin.ModelAdmin):
	form=CompanyForm
	inlines=[CompanyContactInline, CompanyNoteInline]

admin.site.register(Company,CompanyAdmin)

admin.site.register(Eventtype)
admin.site.register(Companytype)
admin.site.register(Contact)
admin.site.register(Contacttype)
admin.site.register(Location)
admin.site.register(Relation)
admin.site.register(Notetype)