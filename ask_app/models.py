#-*- coding: utf-8-*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User, UserManager
from django.db.models import Count
# Create your models here.
#makemigrations
class QuestionManager(models.Manager):
	def get_question_by_id(self, q_id):
		q=self.get(pk=q_id)
		q.answer_count=AnswerManager.get_count_of_answers(Answer.objects,q_id)
		q.tag_list_temp=TagManager.get_tags_by_id_question(Tag.objects,q_id)
		q.tag_list=[]
		for tag in q.tag_list_temp:
			q.tag_list.append(str(tag.value))
		return q
	def get_count_of_answers(self, q_id):
		return AnswerManager.get_count_of_answers(Answer.objects, q_id)
	def get_new_questions(self):
		q_list=self.prefetch_related('author').order_by('-date')[:100]		
		return Question.objects.fill_questions(q_list)
	def get_best_questions(self):
		q_list=self.prefetch_related('author').order_by('-rating')[:100]
		return Question.objects.fill_questions(q_list)
	def fill_questions(self,q_list):
		for q in q_list:
			q.answer_count=AnswerManager.get_count_of_answers(Answer.objects,q.id)			
			q.tag_list=TagManager.get_tags_by_id_question(Tag.objects,q.id)			
		return q_list
	def get_answers_by_id_question(self, q_id):
		return AnswerManager.get_answers_by_id_question(Answer.objects, q_id)
	def get_questions_by_tag(self,tag_value):
		q_list=self.filter(tags__value=tag_value)
		return Question.objects.fill_questions(q_list)
	def get_tags_by_id_question(self, q_id):
		return TagManager.get_tags_by_id_question(Tag.objects,q_id)
class AnswerManager(models.Manager):
	def get_answers_by_id_question(self, q_id):
		a_list=self.filter(question=q_id).order_by('-rating')[:20]
		return a_list
	def get_count_of_answers(self, q_id):
		a=self.filter(question=q_id).count()
		return a
class TagManager(models.Manager):
	def get_tags_by_id_question(self, q_id):
		return self.filter(question=q_id)
	def get_popular_tag(self):
		t_list= self.annotate(question_count=Count('question')).order_by('-question_count')[:10]
		for tag in t_list:
			if tag.question_count>2:
				tag.many=True
			else:
				tag.many=False
		return t_list
	def get_tag_by_value(tag_value):
		return self.get(value=tag_value)
class ProfileManager(models.Manager):
	def get_popular_users(self):
		return self.annotate(question_count=Count('question')).order_by('-question_count')[:5]
	def get_profile(self, user_id):
		return self.get(user__id=user_id)
	def check_unique(self, login):
		return User.objects.filter(username=login).exists()



#Models
class Tag(models.Model):
	value=models.CharField(max_length=15,verbose_name=u'Tag')
	objects=TagManager()	
	class Meta:
		verbose_name=u'Tag'
		verbose_name_plural=u'Tags'
	def __unicode__(self):
		return "{}".format(self.value)

class Profile(models.Model):
	user = models.OneToOneField(User)
	nickname=models.CharField(max_length=30, verbose_name=u'Nickname')
	avatar=models.ImageField(upload_to='avatars/', blank=True, verbose_name=u'Avatar')
	email=models.EmailField(blank=True, verbose_name=u'Email')
	objects=ProfileManager()
	class Meta:
		verbose_name=u'Profile'
		verbose_name_plural=u'Profiles'
	def __unicode__(self):
		return  "{}".format(self.nickname)

class Question(models.Model):
	title= models.CharField(max_length=100,verbose_name=u'Title')
	text= models.TextField(verbose_name=u'Text')
	author = models.ForeignKey('Profile')
	tags=models.ManyToManyField(Tag)
	rating=models.IntegerField(default=0,verbose_name=u'Rating')
	date=models.DateTimeField(auto_now_add=True, verbose_name=u'Date')
	objects=QuestionManager()
	class Meta:
		verbose_name=u'Question'
		verbose_name_plural=u'Questions'
	def __unicode__(self):
		return "{} {} {}".format(self.title,self.author,self.date)

class Answer(models.Model):
	text= models.TextField(verbose_name=u'Text')
	author = models.ForeignKey('Profile',verbose_name=u'User')
	rating=models.IntegerField(default=0,verbose_name=u'Rating')
	question=models.ForeignKey('Question',default=0,verbose_name=u'Question')
	isTrue=models.BooleanField(default=False)
	objects=AnswerManager()
	class Meta:
		verbose_name=u'Answer'
		verbose_name_plural=u'Answers'
	def __unicode__(self):
		return "{} {}".format(self.question.title,self.author)

class LikeQuestion(models.Model):
	user=models.ForeignKey('Profile',verbose_name=u'User')
	question=models.ForeignKey('Question')
	AVAILABLE_VALUE=((1,'like'),(-1,'dislike'),(0,'None'))
	value=models.IntegerField(choices=AVAILABLE_VALUE, blank=True, null=True, verbose_name=u'Value')
	def _unicode__(self):
		return "{} {} {}".format(self.question.title,self.user.nickname,self.value)

class LikeAnswer(models.Model):
	user=models.ForeignKey('Profile',verbose_name=u'User')
	answer=models.ForeignKey('Answer')
	AVAILABLE_VALUE=((1,'like'),(-1,'dislike'),(0,'None'))
	value=models.IntegerField(choices=AVAILABLE_VALUE, blank=True, null=True, verbose_name=u'Value')
	def __unicode__(self):
		return "{} {} {}".format(self.question.title,self.user.nickname,self.value)








