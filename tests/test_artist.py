import unittest
from app_1 import app, artists  # Import the artists list

class ArtistsRouteTest(unittest.TestCase):
    def setUp(self):
        # Create a test client for the application
        self.app = app.test_client()

        # Populate the artists list with sample artists
        artists.clear()  # Clear the list
        artists.extend(["Pixies", "ABBA", "Taylor Swift", "Nina Simone"])


    def test_get_artists(self):
        # Test GET /artists route
        response = self.app.get('/artists')

        # Ensure the status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Ensure the response content is a comma-separated string
        response_data = response.data.decode('utf-8')
        self.assertTrue(isinstance(response_data, str))

        # Ensure that the artists from the response match the sample artists
        expected_artists = "Pixies, ABBA, Taylor Swift, Nina Simone"
        self.assertEqual(response_data, expected_artists)


    def test_create_artist(self):
        # Test POST /artists route
        data = {
            'name': 'Wild nothing',
            'genre': 'Indie'
        }

        response = self.app.post('/artists', data=data)

        # Ensure the status code is 200 OK (no content)
        self.assertEqual(response.status_code, 200)

        # Test GET /artists again to verify the new artist was added
        response = self.app.get('/artists')

        # Ensure the status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Ensure the response content includes the newly added artist
        response_data = response.data.decode('utf-8')
        self.assertIn('Wild nothing', response_data)


