from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json,imagehash,urllib2,io,traceback,sys,numpy,base64
from PIL import Image
# Create your views here.

@csrf_exempt
def index(request):
	message = {}
	if request.method == 'GET':
		if not request.GET.has_key('image'):
			message = construct_message(400,message = 'missing field,invalid request')
		else:
			url = request.GET['image']
			image = get_image_url(url)
			hist = get_vector(image)
			message = construct_message(200,hist = hist)
	elif request.method == 'POST':
		if request.META['CONTENT_TYPE'] == 'application/json':
			paras = json.loads(request.body)
			if not paras.has_key('image'):
				message = construct_message(400,message = 'missing field,invalid request')
			else:
				url = paras['image']
				try:
					image = get_image_url(url)
					hist = get_vector(image)
					message = construct_message(200,hist = hist)
				except Exception as e:
					traceback.print_exc()
					message = construct_message(401,message = str(e))
		elif request.META['CONTENT_TYPE'] == 'application/octet-stream':
				try:
					image = get_image_byte(request.body)
					hist = get_vector(image)
					message = construct_message(200,hist = hist)
				except Exception as e: 
					traceback.print_exc()
					message = construct_message(402,message = str(e))
					print message
	else:
		message = construct_message(403,message = 'unkonw method type')
	return HttpResponse(json.dumps(message))



def construct_message(code,message = None,hist = None):
	print code, message,str(hist)
	mess = {}
	mess['Code'] = code
	if code != 200:
		mess['Message'] = str(message)
	else:
		hist_str = [str(e) for e in hist]
		mess['Message'] = ','.join(hist_str)
	return mess

def get_image_url(url):
	fd = urllib2.urlopen(url)
	image_file = io.BytesIO(fd.read())
	image = Image.open(image_file)
	return image

def get_image_byte(body):
	image = Image.open(io.BytesIO(body))
	return image

def get_vector(image):
	image = image.convert('RGB').resize((100,100),Image.ANTIALIAS)
	nd = numpy.array(image.histogram())
	return [numpy.mean(nd), numpy.median(nd),numpy.std(nd)]



if __name__ == "__main__":
	#url = "http://ww4.sinaimg.cn/large/632dab64jw1f59n36ifk4j208h0dzq42.jpg"
	#url = "http://ww2.sinaimg.cn/large/8c604939jw1f591m2asgsj20dw0kvmzo.jpg"
	#url = "http://ww4.sinaimg.cn/large/6875b119jw1f59ms3vnixj20c30wnn2g.jpg"
	#url = "http://ww3.sinaimg.cn/large/5d523416jw1f58o8e12xlj20ci0crdgm.jpg"
	#url = "http://ww1.sinaimg.cn/large/632dab64jw1f59mo7km4qj20en0adtb0.jpg"
	#url = "http://ww3.sinaimg.cn/large/d6eb2b02jw1f59ml7aeyuj20lw0j6wh3.jpg"
	#url = "http://ww4.sinaimg.cn/mw690/61b889f5gw1f59pgyzjh1j21kw18mk11.jpg"

	url = "http://ww2.sinaimg.cn/mw690/a1ab8e59jw1f59p38thd0j20c83qv7va.jpg"
	image = get_image_url(url)
	hist = get_vector(image)
	print hist
	


