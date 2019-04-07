from django.http import HttpResponse, Http404
import datetime
def hello(request) :
	return HttpResponse("Hello word")

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body> It is now %s.</body></html>" % now
	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)

def test(request):
	print('hello')
	f = open('gp/pages/login.html', 'r+')
	try:
		with open('./pages/login.html', 'r+') as file:
			html = file.read()
			return HttpResponse(html)
	except FileNotFoundError:
		raise Http404()
