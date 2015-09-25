#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re 
from django import template 
from django.contrib.auth.models import Group 

register = template.Library() 

@register.filter(name='has_group') 
def has_group(user, group_name): 
	group = Group.objects.get(name=group_name) 
	return user.groups.filter(name=group_name).exists()

import re 

@register.filter(name='formatcontact')
def formatcontact(string, args): 
	return re.sub('£', args, string)
	
@register.filter(name='linetocomma')
def linetocomma(string): 
	return re.sub('\r\n', ', ', string)
