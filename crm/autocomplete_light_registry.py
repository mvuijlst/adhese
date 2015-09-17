import autocomplete_light.shortcuts
from .models import *

class PersonAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['^firstname', 'lastname']
    model = Person
    choice_html_format = u'<span class="line" data-value="%s">%s</span>'
autocomplete_light.register(PersonAutocomplete)

class RelationAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['name']
    model = Relation
autocomplete_light.register(RelationAutocomplete)

class LocationAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['name', 'address']
    model = Location
autocomplete_light.register(LocationAutocomplete)

class CompanyAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['name']
    model = Company
    choice_html_format = u'<span class="line" data-value="%s">%s</span>'
autocomplete_light.register(CompanyAutocomplete)