from django.contrib import admin

from .models import Person, Contacttype, Contact, Company

admin.site.register(Person)

class ContactAdmin(admin.ModelAdmin):
	list_display = ('date', 'typename')
	search_fields = ['person__firstname', 'person__lastname', 'memo']

admin.site.register(Contact, ContactAdmin)

admin.site.register(Contacttype)
admin.site.register(Company)