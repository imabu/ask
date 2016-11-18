#-*- coding: utf-8-*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.
#makemigrations
class Tag(models.Model):
	value=models.CharField(max_length=15,verbose_name=u'Tag')

class Question(models.Model):
	title= models.CharField(max_length=100,verbose_name=u'Title')
	text= models.TextField(verbose_name=u'Text')
	author = models.ForeignKey('Profile')
	tags=models.ManyToManyField(Tag)
	class Meta:
		verbose_name=u'Question'
		verbose_name_plural=u'Questions'
	def __uncode__(self):
		return self.title

class Profile(User):
	objects = UserManager()
	name= models.CharField(max_length=50,verbose_name=u'Name')
	login = models.CharField(max_length=20,verbose_name=u'Login')
	email = models.EmailField(max_length=20,verbose_name=u'Email')
	class Meta:
		verbose_name=u'User'
		verbose_name_plural=u'Users'
	def __uncode__(self):
		return self.login
class Answer(models.Model):
	text= models.TextField(verbose_name=u'Text')
	author = models.ForeignKey('User')
	tags=models.ManyToManyField(Tag)
	class Meta:
		verbose_name=u'Answer'
		verbose_name_plural=u'Answers'
	def __uncode__(self):
		return self.text
class Like(models.Model):
	user=models.ForeignKey('User')
	question=models.ForeignKey('Question')
	value=((1,'like'),(-1,'dislike'))

