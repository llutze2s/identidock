import unittest
import identidock

class TestCase(unittest.TestCase):

   def setUp(self):            #Testversion initalisiert
       identidock.app.config["TESTING"] = TRUE
       self.app = identidock.app.test_client()

   def test_get_mainpage(self):
       page = self.app.post("/", data=dict(name="Peter"))
       assert page.status_code == 200
       assert 'Hallo' in str(page.data) # Überprüfen ob Hallo im String der Seite vorkommt
       assert 'Peter' in str(page.data) # "    " Peter vorkommt

   def test_html_escaping(self):
       page = self.app.post("/". data=dict(name='"><b>TEST</b><!--"'))
       assert '<b>' not in str(page.data) # Prüfen ob HTML abgefangen wird

if __name__ == '__main__':
   unittest.main()
