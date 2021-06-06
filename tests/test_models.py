import unittest
from app.models import Source, Article

class TestSource(unittest.TestCase):
  def setUp(self):
    self.new_source = Source('argaam','Argaam', 'ارقام موقع متخصص في متابعة سوق الأسهم السعودي تداول - تاسي - مع تغطيه معمقة لشركات واسعار ومنتجات البتروكيماويات , تقارير مالية الاكتتابات الجديده ', 'business', 'http://www.argaam.com' )
  
  def test_instance(self):
    self.assertTrue(isinstance(self.new_source, Source))

  def test_initialization(self):
    self.assertEqual(self.new_source.id, 'argaam')
    self.assertEqual(self.new_source.name, 'Argaam')
    self.assertEqual(self.new_source.description, 'ارقام موقع متخصص في متابعة سوق الأسهم السعودي تداول - تاسي - مع تغطيه معمقة لشركات واسعار ومنتجات البتروكيماويات , تقارير مالية الاكتتابات الجديده ')
    self.assertEqual(self.new_source.category, 'business')
    self.assertEqual(self.new_source.url, 'http://www.argaam.com')

class TestArticle(unittest.TestCase):
  def setUp(self):
    self.new_article = Article('http://www.abc.net.au/news/2021-06-07/vic-covid-lockdown-optimism-next-steps/100194304', 'ABC News' ,'Victorian health officials running "neck-and-neck" with COVID-19 outbreak',"As the end of Victoria's extended lockdown looms, health officials are assessing the next steps in the state's COVID-19 outbreak, which has grown to 70 active cases.", 'https://live-production.wcms.abc-cdn.net.au/11b9c49c382e18ffce7d88caa1cf805f?impolicy=wcms_crop_resize&cropH=2813&cropW=5000&xPos=0&yPos=13&width=862&height=485', '2021-06-06T14:27:59Z')

  def test_instance(self):
    self.assertTrue(isinstance(self.new_article, Article))


  def test_initialization(self):
    self.assertEqual(self.new_article.url, 'http://www.abc.net.au/news/2021-06-07/vic-covid-lockdown-optimism-next-steps/100194304')
    self.assertEqual(self.new_article.author, 'ABC News')
    self.assertEqual(self.new_article.title, 'Victorian health officials running "neck-and-neck" with COVID-19 outbreak')
    self.assertEqual(self.new_article.description, "As the end of Victoria's extended lockdown looms, health officials are assessing the next steps in the state's COVID-19 outbreak, which has grown to 70 active cases.")
    self.assertEqual(self.new_article.urlimg, 'https://live-production.wcms.abc-cdn.net.au/11b9c49c382e18ffce7d88caa1cf805f?impolicy=wcms_crop_resize&cropH=2813&cropW=5000&xPos=0&yPos=13&width=862&height=485')
    self.assertEqual(self.new_article.published, '2021-06-06T14:27:59Z')


if __name__ == '__main__':
  unittest.main()