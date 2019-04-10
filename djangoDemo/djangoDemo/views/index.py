from django.http import HttpResponse
from django.shortcuts import render

def hello1(req):
  # return HttpResponse("hello world")
  ctx = {
      "title": "nice to meet you"
  }
  return render(req, 'hello.html', ctx)

def good(req):
  return HttpResponse("good")
