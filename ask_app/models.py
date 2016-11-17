#-*- coding: utf-8-*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#makemigrations
class Art(models.Model):
	title= models.CharField(max_lenght=255,verbose_name=u'Name')
	text= models.TextField(verbose_name=u'Text')
	is_published = models.BooleanField(default=False, verbose_name=u'Pub')
	author = models.ForeignKey('Author')
	class Meta:
		verbose_name=u'Art'
		verbose_name_plural=u'Arts'
	def __uncode__(self):
		return self.title

class Aut(models.Model):
	name= models.CharField(max_lenght=255,verbose_name=u'Name')
	birth= models.DateField(null=False,blank=False,verbose_name=u'Birth')	
	class Meta:
		verbose_name=u'Aut'
		verbose_name_plural=u'Auts'
	def __uncode__(self):
		return self.title
