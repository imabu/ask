#-*- coding: utf-8-*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.
#makemigrations
class Tag(models.Model):
	value=models.CharField(max_length=15,verbose_name=u'Tag')
	class Meta:
		verbose_name=u'Tag'
		verbose_name_plural=u'Tags'
	def __str__(self):
		return "{}".format(self.value)
class Profile(models.Model):
	profile = models.OneToOneField(User)
	nickname=models.CharField(max_length=30)
	avatar=models.ImageField(upload_to='avatars', blank=True)
	class Meta:
		verbose_name=u'Profile'
		verbose_name_plural=u'Profiles'
	def __str__(self):
		return  "{}".format(self.nickname)
class Question(models.Model):
	title= models.CharField(max_length=100,verbose_name=u'Title')
	text= models.TextField(verbose_name=u'Text')
	author = models.ForeignKey('Profile')
	tags=models.ManyToManyField(Tag)
	rating=models.IntegerField(default=0,verbose_name=u'rating')
	class Meta:
		verbose_name=u'Question'
		verbose_name_plural=u'Questions'
	def __str__(self):
		return "{}".format(self.title)

class Answer(models.Model):
	text= models.TextField(verbose_name=u'Text')
	author = models.ForeignKey('Profile',verbose_name=u'User')
	tags=models.ManyToManyField(Tag)
	rating=models.IntegerField(default=0,verbose_name=u'rating')
	question=models.ForeignKey('Question',default=0,verbose_name=u'Question')
	class Meta:
		verbose_name=u'Answer'
		verbose_name_plural=u'Answers'
	def __str__(self):
		return "{} {}".format(self.question.title)
class LikeQuestion(models.Model):
	user=models.ForeignKey('Profile',verbose_name=u'User')
	question=models.ForeignKey('Question')
	AVAILABLE_VALUE=((1,'like'),(-1,'dislike'))
	value=models.IntegerField(choices=AVAILABLE_VALUE, blank=True, null=True)
	def __str__(self):
		return "{} {} {}".format(self.question.title,self.user.nickname,self.value)
class LikeAnswer(models.Model):
	user=models.ForeignKey('Profile',verbose_name=u'User')
	answer=models.ForeignKey('Answer')
	value=models.IntegerField(blank=True, null=True)
	def __unicode__(self):
		return self.value
