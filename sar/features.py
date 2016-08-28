#coding=utf-8

import getVector
import jieba.posseg as pseg
from snownlp import SnowNLP
import re


def getFV(text):
	if type(text) == str: text = text.decode('utf-8')
	Feature = []
	#print text
	flag,text = location(text)
	if len(text) == 0 : return None
	#print text
	words = pseg.cut(text)
	tokens = []
	for word,x in words:
		tokens.append(word)
	w2v = getVector.get_sentence_vector(tokens)
	Feature.extend(w2v[0])
	Feature.append(size(text))
	Feature.append(at(text))
	Feature.append(link(text))
	Feature.append(sentiment(text))
	Feature.append(time(text))
	Feature.append(emotion(text))
	Feature.append(question(text))
	Feature.append(bang(text))
	Feature.append(dot(text))
	Feature.append(tag(text))
	Feature.append(download(text))
	Feature.append(qing(text))
	Feature.append(blog(text))
	Feature.append(order(text))
	Feature.append(flag)
	return Feature
	
	

def size(text):
	return len(text)
'''
@温泉张兴中 你在吗
'''
def at(text):
	return 1 if '@' in text else 0

'''
从我做起，坚守七条底线，传播正能量！【网络名人达成共识 共守“七条底线”】人民
      网北京8月11日电（记者 贾玥）10日下午，网络名人齐聚央视新址演播厅，对话畅谈网络名人的>      社会责任。 （分享自 @凤凰网） http://t.cn/zQHMhbv 
'''
def link(text):
	return 1 if 'http://' in text else 0

def sentiment(text):
	s = SnowNLP(text)
	return s.sentiments - 0.5

def time(text):
	words = pseg.cut(text)
	flags = []
	for word,flag in words:
		flags.append(flag)
	if 't' in flags: return 1
	p = re.compile(u'.{1,2}月.{1,2}日')
	m = p.search(text)
	return 1 if m != None else 0
	

def emotion(text):
	p = re.compile(u'\[.+\]')
	m = p.search(text)
	return 1 if m != None else 0

'''
这是在哪里拍的？
'''
def question(text):
	'''
1、问事物、时间、处所和数量的主要有8个：谁、何、什么，哪儿、哪里，几时、几、多少
2、问方式、性状和原因的主要有8个：怎、怎么、怎的、怎样、怎么样、怎么着、如何、为什么
语气词主要有4个：吗、呢、吧、啊
疑问副词主要有10个：难道、岂、居然、竟然、究竟、简直、难怪、反倒、何尝、何必
	'''
	flag = u'?$' in text or u'？$' in text or u'[疑问]' in text or u'[思考]' in text or u'?!' in text or u'？！' in text
	return 1 if flag else 0

def bang(text):
	flag = '!' in text or u'！' in text
	return 1 if flag else 0

def dot(text):
	flag = '...' in text or u'。。' in text
	return 1 if flag else 0

'''
#中日关系#【日印决定频繁进行海上联合演习 应对中国影响力】日本首相安倍晋三5月2      9日在官邸与印度总理辛格举行会谈，日印双方决定由日本海上自卫队和印度海军频繁实施定期联
      合演习，以应对中国在海洋加大军事影响力。#大洋战略#
'''
def tag(text):
	p = re.compile(u'(【.+】)|(#.+#)')
	m = p.search(text)
	if m == None:
		return 0
	else:
		return 1

'''
我刚在@微盘 发现了一个很不错的文件"移动互联网7大趋势（完整文字版）.pdf"，推荐
      你也来看看！ http://t.cn/zTw0xMX
'''
def download(text):
	string = u'微盘'
	return 1 if string in text else 0

def qing(text):
	flag = u'请' in text or u'麻烦' in text or u'能不能' in text or u'能否' in text or u'求' in text or u'帮忙' in text
	return 1 if flag else 0 


def blog(text):
	return 1 if u'发表了博文' in text else 0


'''
如果不想让自己的心灵变得荒芜，唯一的方法就是用美德占据自己的心灵！ 我在:http://t.cn/8DeuU5B
'''
'''
@云峰开讲-心灵鸡汤:我是2006级中文二班的，毕业后执教在新疆阿克苏。7年过去了，>      母校变化很大吧，能否发些新校区的相片。好想看到母校的面容。云峰老师，有劳了。 我在:htt      p://t.cn/zH3rlW2
'''
def location(text):
	p = re.compile(u'我在:http://.+')
	newtext = p.sub('',text)
	if newtext == text:
		return (0,text)
	else:
		return (1,newtext)
	#return '我在:http' in text

'''
转【说话的规则】：1）别人的事，小心说，2）长辈的事，
    少说，3）孩子的事，开导地说，4）小事，幽默地说，5）做不到的事
    ，别说，6）伤心的事，只找知心朋友说，7）自己的事，先听听别人>    怎么说，8）夫妻间事，商量着说，9）急事，慢慢说，10）未必会发>    生的事，别胡说，11）伤人的事，绝不说
'''
def order(text):
	flag1 = u'1)' in text and u'2)' in text and u'3)' in text
	flag2 = u'1）' in text and u'2）' in text and u'3）' in text
	flag3 = u'1.' in text and u'2.' in text and u'3.' in text
	flag = flag1 or flag2 or flag3
	return 1 if flag else 0


if __name__ == '__main__':
	print size('如果不想让自己的心灵变得荒芜，唯一的方法就是用美德占据自己的心灵！ 我在:http://t.cn/8DeuU5B')
