from django.http import HttpResponse
def hello(request):
	res=''
	if request.method=='GET':

		res='GET: '
		for key in request.GET:
			res=res+key+' = '+request.GET[key]+' '
	elif request.method=='POST':
		res='POST: '
		for key in request.POST:
			res=res+key+' = '+request.POST[key]+' '
	return HttpResponse(res)
