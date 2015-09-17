from django.db import models

class Company(models.Model):
	name=models.CharField(max_length=150)
	address=models.TextField(null=True,blank=True)
	
	class Meta:
		verbose_name_plural = 'Companies'
		
	def __str__(self):
		 return self.name

class Person(models.Model):
	firstname=models.CharField(max_length=150)
	lastname=models.CharField(max_length=150)
	company=models.ForeignKey(Company,null=True,blank=True)
	
	def __str__(self):
		 return self.firstname + " " + self.lastname 

class Contacttype(models.Model):
	typename=models.CharField(max_length=50)
	
	def __str__(self):
		 return self.typename 

class Contact(models.Model):
	date=models.DateField('contact date',null=True,blank=True)
	typename=models.ForeignKey(Contacttype,null=True,blank=True)
	persons=models.ManyToManyField(Person,null=True,blank=True)
	memo=models.TextField(null=True,blank=True)
	nextdate=models.DateTimeField('next date',null=True,blank=True)
	
	def __str__(self):
		 return str(self.date)