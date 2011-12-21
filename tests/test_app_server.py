import unittest
from PyLakitu import app

class ServerTestCase(unittest.TestCase):
    '''
    This tests the functionality of the server

    HTTP requests are generated and expected responses
    are asserted.
    '''
    def setUp(self):
        #Initialize a test client to the server
        self.app = app.test_client()

    def test_get(self):
        #This tests the routing to the index
        rv = self.app.get('/')
        assert "This is the index method" in rv.data

    def test_post(self):
        #This tests posting to the update route
        rv = self.app.post('/update')
        assert "This is the update method" in rv.data

    def test_post_val(self):
        #This tests posting a value to the update_n route
        rv = self.app.post('/update_n/300')
        assert "300" in rv.data

if __name__ == '__main__':
    unittest.main()
