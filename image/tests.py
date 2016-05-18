from django.test import TestCase
import views

# Create your tests here.

class ihash(TestCase):
	
	def test_get_hash(self):
		url = 'https://www.baidu.com/img/bd_logo1.png'
		sign = views.get_hash(url)
		self.assertEqual('000008c2b061debf',sign)


if __name__ == '__main__':
	unittest.main()
