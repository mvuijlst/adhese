from django.contrib import admin

from .models import Person, Eventtype, Event, Company, Relation, Companytype, Contact, Contacttype, Project, Location

class ContactInline(admin.TabularInline):
	model=Contact
	extra=0

class PersonAdmin(admin.ModelAdmin):
	inlines=[ContactInline]
	list_display = ('firstname', 'lastname', 'company')
	search_fields = ['firstname', 'lastname', 'company__name']

admin.site.register(Person,PersonAdmin)

class EventAdmin(admin.ModelAdmin):
	list_display = ('datetime', 'eventtype', 'project')
	search_fields = ['person__firstname', 'person__lastname', 'memo']

admin.site.register(Event, EventAdmin)

admin.site.register(Eventtype)
admin.site.register(Company)
admin.site.register(Relation)
admin.site.register(Companytype)
admin.site.register(Contact)
admin.site.register(Contacttype)
admin.site.register(Project)
admin.site.register(Location)