import unittest
from flask import Flask
import requests

class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)

        @self.app.route('/')
        def hello():
            return 'Hello, Flask!'

    def test_flask_running(self):
        base_url = 'https://save-sync.onrender.com'
        response = requests.get(f'{base_url}')
        self.assertEqual(response.status_code, 200)
        

if __name__ == '__main__':
    unittest.main()
