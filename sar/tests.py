#coding=utf-8
from django.test import TestCase
import features
import jieba

# Create your tests here.

class sarTest(TestCase):
	def setUp(self):
		self.text = u'今天天气不错'
		self.text1 = u'今天天气不错 @abc'
		self.text2 = u'今天天气不错 @abc http://124.com'
		self.tt = u'从我做起，坚守七条底线，传播正能量！【网络名人达成共识 共守“七条底线”】人民网北京8月11日电（记者 贾）10日下午，网络名人齐聚央视新址演播厅，对话畅谈网络名人的社会责任。 （分享自 @凤凰网） http://t.cn/zQHMhbv'
		self.tt1 = u'日本首相安倍晋三5月29日在官邸与印度总理辛格举行会谈'
		self.tt2 = u'日本首相安倍晋三5月29日在官邸与印度总理辛格举行会谈[不开心]'
		self.tt3 = u'这是在哪里拍的？！！'
		self.tt4 = u'好郁闷哈。。'
		self.tt5 = u'what can i do for you ...'
		self.tt6 = u'#中日关系#【日印决定频繁进行海上联合演习 应对中国影响力】日本首相安倍晋三5月29日在官邸与印度总理辛格举行会谈，日印双方决定由日本海上自卫队和印度海军频繁实施定期联合演习，以应对中国在海洋加大军事影响力。#大洋战略#'
		self.tt7=u'我刚在@微盘 发现了一个很不错的文件"移动互联网7大趋势（完整文字版）.pdf"，推荐你也来看看！ http://t.cn/zTw0xMX'
		self.tt8=u'@abc 请你们放尊重一点把'
		self.tt9=u'@abc 麻烦放尊重一点把'
		self.tt10=u'我们发表了博文'
		self.tt11 = u'@云峰开讲-心灵鸡汤:我是2006级中文二班的，毕业后执教在新疆阿克苏。7年过去了,母校变化很大吧，能否发些新校区的相片。好想看到母校的面容。云峰老师，有劳了。 我在:http://t.cn/zH3rlW2'
		self.tt12 = u'@云峰开讲-心灵鸡汤:我是2006级中文二班的，毕业后执教在新疆阿克苏。7年过去了,母校变化很大吧，能否发些新校区的相片。好想看到母校的面容。云峰老师，有劳了。 '
		self.tt13 = u'转【说话的规则】：1）别人的事，小心说，2）长辈的事，少说，3）孩子的事，开导地说，4）小事，幽默地说，5）做不到的事，别说，6）伤心的事，只找知心朋友说，7）自己的事，先听听别人怎么说，8）夫妻间事，商量着说，9）急事，慢慢说，10）未必会发生的事，别胡说，11）伤人的事，绝不说'
	

	def test_get_size(self):
		self.assertEquals(6,features.size(self.text))


	def test_at(self):
		self.assertEquals(0,features.at(self.text))
		self.assertEquals(1,features.at(self.text1))

	def test_link(self):
		self.assertEquals(0,features.link(self.text1))
		self.assertEquals(1,features.link(self.text2))
	
	def test_sentiment(self):
		self.assertEquals(0.21203743673100572,features.sentiment(self.text1))
		self.assertEquals(0.18998799176337644,features.sentiment(self.text2))
	
	def test_time(self):
		
		self.assertEquals(1,features.time(self.tt1))
		self.assertEquals(1,features.time(self.tt))

	def test_emotion(self):
		self.assertEquals(0,features.emotion(self.tt))
		self.assertEquals(1,features.emotion(self.tt2))

	def test_question(self):
		self.assertEquals(0,features.question(self.tt))
		self.assertEquals(1,features.question(self.tt3))

	
	def test_bang(self):
		self.assertEquals(1,features.bang(self.tt))
		self.assertEquals(1,features.bang(self.tt3))

	def test_dot(self):
		self.assertEquals(0,features.dot(self.tt3))
		self.assertEquals(1,features.dot(self.tt4))
		self.assertEquals(1,features.dot(self.tt5))

	def test_tag(self):
		self.assertEquals(1,features.tag(self.tt))
		self.assertEquals(1,features.tag(self.tt6))
		self.assertEquals(0,features.tag(self.tt5))

	def test_download(self):
		self.assertEquals(1,features.download(self.tt7)) 

	def test_qing(self):
		self.assertEquals(1,features.qing(self.tt8))
		self.assertEquals(1,features.qing(self.tt9))

	def test_blog(self):
		self.assertEquals(1,features.blog(self.tt10))
		self.assertEquals(0,features.blog(self.tt11))
	
	def test_location(self):
		self.assertEquals((1,self.tt12),features.location(self.tt11))

	def test_order(self):
		self.assertEquals(1,features.order(self.tt13))

	def test_FV(self):
		print features.getFV(self.tt11)
		
		


if __name__ == '__main__':
	unittest.main()
