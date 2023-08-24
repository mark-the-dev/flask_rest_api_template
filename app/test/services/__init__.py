import unittest
from main import create_app, db
"""
This is a super class for testing any services
"""
class TestService(unittest.TestCase):
    def setUp(self):
        self.app = create_app("test")
        self.db = db
        
    def tearDown(self):
        with self.app.app_context():
            self.db.session.remove()
            self.db.drop_all()
