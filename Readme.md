## Introduction
this program is to provide several basic service with django

## Available service
1. chinese sentiment(using snownlp) 
2. signature for image(using imagehash)
3. image\'s color histogram
4. image ocr service
5. text speech act classification


## usage
pip -r requirements.txt
cd olnlp
python manage.py runserver 0.0.0.0:8000

##API
chinese sentiment: 
	POST -- http://ip:port/snow/ {'text':text}  
image signature:
	POST -- http://ip:port/image/ {'image':url}  
image histgram:
	POST -- http://ip:port/hist/ {'image':url}
ocr(both english and chinese):
	POST -- http://ip:port/ocr/ {'image':url}

## Notice
For GET method, there is so much limitation about the text such as symbols.
We can simplely deactive csrf.
Otherwise we need to use other framework.

## [dhash](http://blog.iconfinder.com/detecting-duplicate-images-using-python/)
1. Grayscale the image
2. shrink the image to a common size (9*8)
3. compare adjacent pixels if bigger
4. get boolean matrix and change it to a hash signature.

## [tesseract-ocr]
1. dependency for ocr service
2. install command: sudo apt-get install tesseract-ocr && sudo apt-get install tesseract-ocr-chi-sim (model and data version should be matched.)

