#-*- coding: utf-8-*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.
#makemigrations
class Tag(models.Model):
	value=models.CharField(max_length=15,verbose_name=u'Tag')
class Profile(User):
	objects = UserManager()
	avatar=models.ImageField(upload_to='avatars')
	class Meta:
		verbose_name=u'User'
		verbose_name_plural=u'Users'
	def __uncode__(self):
		return self.login
class Question(models.Model):
	title= models.CharField(max_length=100,verbose_name=u'Title')
	text= models.TextField(verbose_name=u'Text')
	author = models.ForeignKey('Profile')
	tags=models.ManyToManyField(Tag)
	rating=models.IntegerField(default=0,verbose_name=u'rating')
	class Meta:
		verbose_name=u'Question'
		verbose_name_plural=u'Questions'
	def __uncode__(self):
		return self.title

class Answer(models.Model):
	text= models.TextField(verbose_name=u'Text')
	author = models.ForeignKey('Profile',verbose_name=u'User')
	tags=models.ManyToManyField(Tag)
	rating=models.IntegerField(default=0,verbose_name=u'rating')
	question=models.ForeignKey('Question',default=0,verbose_name=u'Question')
	class Meta:
		verbose_name=u'Answer'
		verbose_name_plural=u'Answers'
	def __uncode__(self):
		return self.text
class LikeQuestion(models.Model):
	user=models.ForeignKey('Profile',verbose_name=u'User')
	question=models.ForeignKey('Question')
	value=((1,'like'),(-1,'dislike'))
class LikeAnswer(models.Model):
	user=models.ForeignKey('Profile',verbose_name=u'User')
	answer=models.ForeignKey('Answer')
	value=((1,'like'),(-1,'dislike'))
