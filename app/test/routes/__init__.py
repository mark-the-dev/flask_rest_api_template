import unittest
from main import create_app

class TestAPIResource(unittest.TestCase):
    def setUp(self):
        self.app = create_app("test").test_client()