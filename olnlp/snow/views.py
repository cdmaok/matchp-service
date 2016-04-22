from django.shortcuts import render
from django.http import HttpResponse
import snownlp
# Create your views here.

def index(request):
	text = request.GET['text']
	if text.strip() == '':
		return HttpResponse('empty text')
	else:
		return HttpResponse("Hello----world")
