from django.contrib import admin

from .models import Person, Contacttype, Contact, Company

admin.site.register(Person)
admin.site.register(Contact)
admin.site.register(Contacttype)
admin.site.register(Company)