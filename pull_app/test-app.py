import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Unit Test 1: Test the read page
    def test_read_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    # Unit Test 2: Test adding an item
    def test_add_item(self):
        response = self.app.post('/add', data=dict(item="Test Item"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # Integration Test: Test adding an item and then reading it
    def test_add_and_read_item(self):
        self.app.post('/add', data=dict(item="Test Item"), follow_redirects=True)
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Item', response.data)
        
"""
if __name__ == '__main__':
    unittest.main()
    print("Test completed successfully")"""

if __name__ == '__main__':
    # Create a test suite
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestFlaskApp)

    # Create a test runner with output to a file
    with open('test_results.txt', 'w') as f:
        test_runner = unittest.TextTestRunner(stream=f, verbosity=2)
        
        # Run the tests and write the output to the file
        result = test_runner.run(test_suite)
    
    # Check if the tests completed successfully
    if result.wasSuccessful():
        print("Test completed successfully")
    else:
        print("Test failed")
