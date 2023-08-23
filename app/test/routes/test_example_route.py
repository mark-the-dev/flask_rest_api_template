import unittest
from . import TestAPIResource

class TestExampleRoute(TestAPIResource):
    
    def test_get_example(self):
        response = self.app.get('/api/example')
        self.assertEqual(response.status_code, 200)
    
if __name__ == '__main__':
    unittest.main()