from django.http import HttpResponse

def hello(req):
  return HttpResponse("hello world")
