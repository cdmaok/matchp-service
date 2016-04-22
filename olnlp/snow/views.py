from django.shortcuts import render
from django.http import HttpResponse
import json
from snownlp import SnowNLP
# Create your views here.

def index(request):
	message = {}
	if not request.GET.has_key('text'):
		message['Code'] = '400'
		message['Message'] = 'invalid request'
	else:
		text = request.GET['text']
		if text.strip() == '':
			message['Code'] = '406'
			message['Message'] = 'empty text'
		else:
			s = SnowNLP(text)
			score =  s.sentiments
			print score
			message['Code'] = '200'
			message['Message'] = score

	return HttpResponse(json.dumps(message))
