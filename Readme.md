## Introduction
this program is to wrap snownlp with django


## usage
pip -r requirements.txt
cd olnlp
python manage.py runserver 0.0.0.0:8000

##API
GET -- http://ip:port/snow/?text=xxxx
POST -- http://ip:port/snow/

##Notice
For GET method, there is so much limitation about the text such as symbols.
We can simplely deactive csrf.
Otherwise we need to use other framework.

