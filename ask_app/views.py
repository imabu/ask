from django.shortcuts import render
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse
# Create your views here.
def index(request):
	questions=[]
	t =get_template('index.html')
	for i in range(1,10):
		questions.append({'title': 'title'+str(i), 'text':'text','author': 'user '+str(i),'rating':i, 'tags':[str(i), 'tag'+str(i)]},)	
	context={'questions':questions}	
	return render(request,'index.html',context)

def signup(request):
	return render(request,'signup.html')
 
def question_detail(request, question_id):
	t=get_template('question.html')
	question_details={'question_id':question_id,'title':'title'+str(question_id), 'text':'text','author': 'user '+str(question_id),'rating':question_id, 'tags':[str(question_id), 'tag'+str(question_id)]}
	context={'question_details':question_details}
	return render(request, 'question.html', context)

def login(request):
	return render(request,'login.html')

def settings(request):
	user_data={'login':'user','email':'smth@smth.com','nickname':'user_1'}
	context={'user_data':user_data}
	return render(request,'settings.html',context)

def ask(request):
	return render(request,'ask.html')

def hot(request):
	questions=[]
	t =get_template('index.html')
	for i in range(1,10):
		questions.append({'title': 'title'+str(i), 'text':'text','author': 'user '+str(i),'rating':i, 'tags':[str(i), 'tag'+str(i)]},)
	context={'questions':questions}
	return render(request,'index.html',context)

def tag(request,tag):
	t=get_template('tag.html')
	for i in range(1,10):
		questions.append({'tag':tag,'title': 'title'+str(i), 'text':'text','author': 'user '+str(i),'rating':i, 'tags':[str(i), 'tag'+str(i)]},)
	context={'tag_questions':questions}
	return render(request,'tag.html',context)
