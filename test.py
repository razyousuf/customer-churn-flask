import unittest
from app import app

class FlaskTest(unittest.TestCase):

    # Test if the home page loads correctly
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.status_code, 200)

    # Test if the about page loads correctly
    def test_about(self):
        tester = app.test_client(self)
        response = tester.get("/about")
        self.assertEqual(response.status_code, 200)

    # Test the prediction endpoint with valid input
    def test_prediction(self):
        tester = app.test_client(self)
        response = tester.post("/", data={
            'tenure': '12',
            'MonthlyCharges': '70.5',
            'TotalCharges': '840.0',
            'dependents': '1',
            'internetservice': 'fiber_optic',
            'onlinesecurity': 'no',
            'onlinebackup': 'no',
            'deviceprotection': 'no',
            'techsupport': 'no',
            'streamingtv': 'no_internet_service',
            'streamingmovies': 'no_internet_service',
            'contract': '1_year',
            'paperlessbilling': '1',
            'paymentmethod': 'electronic_check'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"This customer is likely", response.data)

if __name__ == "__main__":
    unittest.main()
