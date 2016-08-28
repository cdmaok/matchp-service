from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json,pytesseract,urllib2,io,traceback,sys,numpy,base64
from PIL import Image

@csrf_exempt
def index(request):
	message = {}
	if request.method == 'GET':
		if not request.GET.has_key('image'):
			message = construct_message(400,message = 'missing field,invalid request')
		else:
			url = request.GET['image']
			image = get_image_url(url)
			hist = get_ocr(image)
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
					hist = get_ocr(image)
					message = construct_message(200,hist = hist)
				except:
					traceback.print_exc()
					message = construct_message(400,message = sys.exc_info()[0])
		elif request.META['CONTENT_TYPE'] == 'application/octet-stream':
				try:
					image = get_image_byte(request.body)
					hist = get_ocr(image)
					message = construct_message(200,hist = hist)
				except: 
					traceback.print_exc()
					message - construct_message(400,message = sys.exc_info()[0])
	else:
		message = construct_message(400,message = 'unkonw method type')
	return HttpResponse(json.dumps(message))



def construct_message(code,mess = None,hist = None):
	message = {}
	message['Code'] = code
	if code != 200:
		message['Message'] = str(mess)
	else:
		hist_str = [str(e) for e in hist]
		message['Message'] = ','.join(hist_str)
	return message

def get_image_url(url):
	fd = urllib2.urlopen(url)
	image_file = io.BytesIO(fd.read())
	image = Image.open(image_file)
	return image

def get_image_byte(body):
	image = Image.open(io.BytesIO(body))
	return image

def get_ocr(image):
        eng = pytesseract.image_to_string(image,lang='eng')
        chi = pytesseract.image_to_string(image,lang='chi_sim')
        return [transform(eng), transform(chi)]

def transform(text):
        if text == '': 
                return 0
        else:
                return len(text)



if __name__ == "__main__":
	#url = "http://ww4.sinaimg.cn/large/632dab64jw1f59n36ifk4j208h0dzq42.jpg"
	#url = "http://ww2.sinaimg.cn/large/8c604939jw1f591m2asgsj20dw0kvmzo.jpg"
	url = "http://ww4.sinaimg.cn/large/6875b119jw1f59ms3vnixj20c30wnn2g.jpg"
	#url = "http://ww3.sinaimg.cn/large/5d523416jw1f58o8e12xlj20ci0crdgm.jpg"
	#url = "http://ww1.sinaimg.cn/large/632dab64jw1f59mo7km4qj20en0adtb0.jpg"
	#url = "http://ww3.sinaimg.cn/large/d6eb2b02jw1f59ml7aeyuj20lw0j6wh3.jpg"
	#url = "http://ww4.sinaimg.cn/mw690/61b889f5gw1f59pgyzjh1j21kw18mk11.jpg"

	#url = "http://ww2.sinaimg.cn/mw690/a1ab8e59jw1f59p38thd0j20c83qv7va.jpg"
	image = get_image_url(url)
	sign = get_ocr(image)
	print sign
	


