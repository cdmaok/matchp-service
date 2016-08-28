from django.test import TestCase
import views

# Create your tests here.
class ImageOcr(TestCase):

	def test_get_ocr_string(self):
		url = 'http://ww3.sinaimg.cn/mw690/5396ee05jw1f4enwt68u9j20p30iuacj.jpg'
		ocr_feature = views.get_ocr_string(url)
		print ocr_feature
		self.assertEqual([561,855],ocr_feature)
		url = 'http://ww3.sinaimg.cn/mw690/0066MJptgw1f4d52ith5zj30dw099jsk.jpg'
		ocr_feature = views.get_ocr_string(url)
		print ocr_feature
		self.assertEqual([0,0],ocr_feature)
		url = 'http://ww4.sinaimg.cn/mw690/684ff39bjw1f4frcnzzokj20cs0a8gmf.jpg'
		print ocr_feature 
		

if __name__ == '__main__':
	unittest.main()
