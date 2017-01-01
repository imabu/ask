#-*- coding: utf-8-*-
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate,login,logout
from django.template.context_processors import csrf
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ask_app.models import *
from django.contrib import auth 
from ask_app.forms import *
from django.core.files.uploadedfile import SimpleUploadedFile


def index(request):	
	questions=Question.objects.get_new_questions()
	popular_tag=Tag.objects.get_popular_tag()
	popular_users=Profile.objects.get_popular_users()
	page=paginate(request, questions)
	questions=page	
	isAuth=auth.get_user(request).username
	#profile=None
	#if isAuth:	
		#profile=Profile.objects.get_profile(auth.get_user(request).id)
	#context = {'page':page, 'questions':questions,'popular_tag':popular_tag, 'popular_users':popular_users,'isAuth':isAuth,'profile':profile}
	context = {'page':page, 'questions':questions,'popular_tag':popular_tag, 'popular_users':popular_users,'isAuth':isAuth}
	return render(request,'index.html',context)

def signup(request):
	context={}
	context.update(csrf(request))
	context['form']=RegistrationForm()
	if request.POST:
		form=RegistrationForm(request.POST, request.FILES)
		context['form']=form
		if form.is_valid():
			form.save()

			#username=form.cleaned_data['username']
			#nickname=form.cleaned_data['nickname']
			#email=form.cleaned_data['email']
			#avatar=request.FILES.get('avatar','')
			#user=User.objects.get(username=username)

			#new_profile=Profile(user=user,nickname=nickname, avatar=avatar)
			#new_profile.save()

			return redirect('/login/')
		else:
			context['form']=RegistrationForm()
	return render_to_response('signup.html',context)
	
def question_detail(request, question_id):
	question_details=Question.objects.get_question_by_id(question_id)
	popular_tag=Tag.objects.get_popular_tag()
	popular_users=Profile.objects.get_popular_users()
	comments=Answer.objects.get_answers_by_id_question(question_id)
	context={'question_details':question_details,'comments':comments,'isAuth':auth.get_user(request).username, 'popular_tag':popular_tag, 'popular_users':popular_users}
	return render(request, 'question.html', context)

def _login(request):
	if request.POST:
		username=request.POST.get('username','')
		password=request.POST.get('password','')
		user=authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect("/")			
		else:
			context = {'error_login': 1}
			return render(request,'login.html',context)
	else:
		context = {'isAuth': 0}
	return render(request,'login.html',context)
def _logout(request):
	logout(request)
	return redirect("/")

def settings(request):
	popular_tag=Tag.objects.get_popular_tag()
	popular_users=Profile.objects.get_popular_users()
	user_data={'login':'user','email':'smth@smth.com','nickname':'user_1'}
	context={'user_data':user_data,'isAuth':auth.get_user(request).username,'popular_tag':popular_tag, 'popular_users':popular_users}
	return render(request,'settings.html',context)

def ask(request):
	popular_tag=Tag.objects.get_popular_tag()
	popular_users=Profile.objects.get_popular_users()
	context = {'isAuth': auth.get_user(request).username,'popular_tag':popular_tag, 'popular_users':popular_users}
	return render(request,'ask.html',context)

def hot(request):
	questions=Question.objects.get_best_questions()
	popular_tag=Tag.objects.get_popular_tag()
	popular_users=Profile.objects.get_popular_users()
	page=paginate(request, questions)
	questions=page
	context = {'page':page, 'questions':questions,'popular_tag':popular_tag, 'popular_users':popular_users, 'isAuth':auth.get_user(request).username}
	return render(request,'hot.html',context)

def tag(request,tag):
	popular_tag=Tag.objects.get_popular_tag()
	popular_users=Profile.objects.get_popular_users()
	questions=Question.objects.get_questions_by_tag(tag)
	page=paginate(request, questions)
	questions=page
	context={'page':page,'questions':questions,'tag':tag,'isAuth':True,'popular_tag':popular_tag, 'popular_users':popular_users,'isAuth': auth.get_user(request).username}
	return render(request,'tag.html',context)

def paginate(request,questions):
	paginator = Paginator(questions, 5)
	pageNum = request.GET.get('page')
	try:
		page = paginator.page(pageNum)
		if pageNum != None:
			pageNum = int(pageNum)		
	except PageNotAnInteger:
		page = paginator.page(1)
		pageNum = 1
	except EmptyPage:
		page = paginator.page(1)
		pageNum = 1
	#page.page_range_current = get_page_range(pageNum, paginator)
	return page
