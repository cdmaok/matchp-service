from django.test import TestCase
import views

# Create your tests here.

class ihist(TestCase):
	
	def test_get_hist(self):
		url = 'https://www.baidu.com/img/bd_logo1.png'
		print 'bd',views.get_hist(url)
		url = 'http://ww3.sinaimg.cn/mw690/5396ee05jw1f4enwt68u9j20p30iuacj.jpg'
		print 'mid',views.get_hist(url)
		url = 'http://ww1.sinaimg.cn/mw690/6ba51bbbgw1f4ehimrrm1j20m1bw7e85.jpg'
		print 'longt',views.get_hist(url)
		url = 'http://ww1.sinaimg.cn/mw690/a02cee3bjw1f4eih33kbyj20ck0o8jth.jpg'
		print 'longt',views.get_hist(url)
		url = 'http://ww3.sinaimg.cn/mw690/718878b5jw1f4ei18txcpj20ku0dumyu.jpg'
		print 'longt',views.get_hist(url)
		url = 'http://ww1.sinaimg.cn/mw690/972a1170jw1f4eh7vu4yqj20ko0ktk2b.jpg'
		print 'longt',views.get_hist(url)


if __name__ == '__main__':
	unittest.main()
