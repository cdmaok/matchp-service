from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from snownlp import SnowNLP
# Create your views here.

@csrf_exempt
def index(request):
	message = {}
	print request.method
	if request.method == 'GET':
		message = construct_message(request.GET,'text')
	elif request.method == 'POST':
		print '%r' %request
		message = construct_message(json.loads(request.body),'text')
	else:
		print 'invalid request'
	return HttpResponse(json.dumps(message))


def construct_message(parameter,key):
	message = {}
	if not parameter.has_key(key):
		message['Code'] = 400
		message['Message'] = 'invalid request'
	else:
		text = parameter[key]
		if text.strip() == '':
			message['Code'] = 406
			message['Message'] = 'empty text'
		else:
			s = SnowNLP(text)
			score =  s.sentiments
			print text,score
			message['Code'] = 200
			message['Message'] = score
	return message

