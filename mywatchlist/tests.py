from django.test import TestCase, Client

class MyWatchlistTest(TestCase):

    def test_mywatchlist_html_url_exists(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)
    
    def test_mywatchlist_xml_url_exists(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_mywatchlist_json_url_exists(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)