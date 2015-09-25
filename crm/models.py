from django.db import models

class Companytype(models.Model):
	typename=models.CharField(max_length=50)
	
	class Meta:
		ordering = ['typename']
		verbose_name = 'Company type'
		verbose_name_plural = 'Company types'
	
	def __str__(self):
		 return self.typename 

class Relation(models.Model):
	name=models.CharField(max_length=50)
	
	class Meta:
		ordering = ['name']
		
	def __str__(self):
		 return self.name 

class Location(models.Model):
	name=models.CharField(max_length=150)
	address=models.TextField(null=True,blank=True)
	
	class Meta:
		ordering = ['name']
		
	def __str__(self):
		 return self.name

class Company(models.Model):
	name=models.CharField(max_length=150)
	address=models.TextField(null=True,blank=True)
	logo=models.ImageField(upload_to='logo',null=True,blank=True)
	typename=models.ForeignKey(Companytype,null=True,blank=True)
	relation=models.ForeignKey(Relation,null=True,blank=True)
	
	class Meta:
		ordering = ['name']
		verbose_name_plural = 'Companies'
		
	def __str__(self):
		 return self.name

class Person(models.Model):
	firstname=models.CharField(max_length=150,null=True,blank=True)
	lastname=models.CharField(max_length=150)
	function=models.CharField(max_length=150,null=True,blank=True)
	company=models.ForeignKey(Company,null=True,blank=True)
	photo = models.ImageField(upload_to='photo',null=True,blank=True)
	
	class Meta:
		ordering = ['lastname', 'firstname']
		
	def __str__(self):
		 return self.firstname + " " + self.lastname 

class Eventtype(models.Model):
	name=models.CharField(max_length=50)
	
	class Meta:
		verbose_name = 'Event type'
		verbose_name_plural = 'Event types'
		ordering = ['name']
	
	def __str__(self):
		 return self.name 

class Project(models.Model):
	name=models.CharField(max_length=50)
	memo=models.TextField(null=True,blank=True)
	active=models.BooleanField(default=True)
	
	class Meta:
		ordering = ['name']
		
	def __str__(self):
		 return self.name 

class Event(models.Model):
	datetime=models.DateTimeField('Date/time',null=True,blank=True)
	subject=models.CharField(max_length=200,null=True,blank=True)
	eventtype=models.ForeignKey(Eventtype,null=True,blank=True)
	location=models.ForeignKey(Location,null=True,blank=True)
	project=models.ForeignKey(Project,null=True,blank=True)
	persons=models.ManyToManyField(Person)
	meetingnotes=models.CharField(max_length=200,null=True,blank=True)
	nextevent=models.ForeignKey('self',null=True,blank=True)
	
	class Meta:
		ordering = ['datetime']
	
	def __str__(self):
		 return str(self.datetime) + " " + self.eventtype.name

class Contacttype(models.Model):
	name = models.CharField(max_length=50)
	template = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name
	
	class Meta:
		ordering = ['name']
		verbose_name = 'Means of contact'
		verbose_name_plural = 'Means of contact'

class Notetype(models.Model):
	name = models.CharField(max_length=50)
	icon = models.CharField(max_length=50)
	
	def __str__(self):
		return self.name
	
	class Meta:
		ordering = ['name']
		
class Contact(models.Model):
	person=models.ForeignKey(Person,null=True,blank=True)
	company=models.ForeignKey(Company,null=True,blank=True)
	contacttype=models.ForeignKey(Contacttype)
	contactdata=models.CharField(max_length=200)
	remark=models.CharField(max_length=150,null=True,blank=True)
	valid=models.BooleanField(default=True)
	
	class Meta:
		ordering = ['contacttype']
		
	def __str__(self):
		return self.contacttype.name + " " + self.contactdata

class Note(models.Model):
	datetime=models.DateTimeField('Date/time', auto_now_add=True)
	person=models.ForeignKey(Person, null=True, blank=True)
	company=models.ForeignKey(Company, null=True, blank=True)
	event=models.ForeignKey(Event, null=True, blank=True)
	project=models.ForeignKey(Project, null=True, blank=True)
	note=models.TextField()
	notetype=models.ForeignKey(Notetype)
	actiondate=models.DateField('Action by', null=True, blank=True)
	actionperson=models.ForeignKey(Person, related_name='note_actionperson', null=True, blank=True)
	
	class Meta:
		ordering = ['datetime']
		
	def __str__(self):
		return self.notetype.name+ " " + self.datetime.strftime('%Y-%m-%d %H:%M') 