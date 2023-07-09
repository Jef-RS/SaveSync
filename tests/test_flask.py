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
        response = requests.get('http://localhost:5000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Hello, Flask!')

if __name__ == '__main__':
    unittest.main()
