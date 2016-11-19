from django.shortcuts import render
from django.template.loader import get_template
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
	questions=[]
	t =get_template('index.html')
	for i in range(1,10):
		questions.append({'question_id':i,'title': 'title'+str(i), 'text':'text','author': 'user '+str(i),'rating':i, 'tags':[str(i), 'tag'+str(i)]},)
	context={'questions':questions, 'isAuth':True}
	return render(request,'index.html',context)

def signup(request):
	return render(request,'signup.html')
 
def question_detail(request, question_id):
	t=get_template('question.html')
	question_details={'question_id':question_id,'title':'title'+str(question_id), 'text':'text','author': 'user '+str(question_id),'rating':question_id, 'tags':[str(question_id), 'tag'+str(question_id)]}
	comments=[]
	for i in range(1,5):
		comments.append({'text':'text','author': 'user '+str(i),'rating':i,'isTrue':True})
	context={'question_details':question_details,'comments':comments,'isAuth':True}
	return render(request, 'question.html', context)

def login(request):
	context = {'isAuth': 0}
	return render(request,'login.html',context)

def settings(request):
	user_data={'login':'user','email':'smth@smth.com','nickname':'user_1'}
	context={'user_data':user_data,'isAuth':True}
	return render(request,'settings.html',context)

def ask(request):
	context = {'isAuth': True}
	return render(request,'ask.html',context)

def hot(request):
	questions=[]
	t =get_template('index.html')
	for i in range(1,10):
		questions.append({'question_id':i,'title': 'title'+str(i), 'text':'text','author': 'user '+str(i),'rating':i, 'tags':[str(i), 'tag'+str(i)]},)
	context={'questions':questions,'isAuth':False}
	return render(request,'index.html',context)

def tag(request,tag):
	questions=[]
	t=get_template('tag.html')
	for i in range(1,10):
		questions.append({'question_id':i,'title': 'title'+str(i), 'text':'text','author': 'user '+str(i),'rating':str(i), 'tags':[str(i), 'tag'+str(i)]},)
	context={'questions':questions,'tag':tag,'isAuth':True}
	return render(request,'tag.html',context)


def paginator(request):
	questions = question.objects.all()
	paginator = Paginator(questions, 10)
	page = self.request.GET.get('page')
	try:
		questions = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		questions = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		questions = paginator.page(paginator.num_pages)
	return questions
