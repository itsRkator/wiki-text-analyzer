# test_app.py
import unittest
from main import app

# End point test variables
WORD_FREQUENCY_ENDPOINT = "/word_frequency"
SEARCH_HISTORY_ENDPOINT = "/search_history"


# Test cases for the Wikipedia API


class WikipediaAPITestCase(unittest.TestCase):

    def setUp(self):
        # Set up a test client
        self.app = app.test_client()
        # Initialize search history for testing
        app.search_history = [
            {"topic": "Python", "top_words": [("python", 10), ("language", 5)]}
        ]

    async def test_word_frequency_endpoint(self):
        # Test the Word Frequency Analysis Endpoint with data in the request body

        # Typical use case
        response = await self.app.post(
            WORD_FREQUENCY_ENDPOINT, json={"topic": "Python", "n": 5}
        )
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn("topic", data)
        self.assertIn("top_words", data)

        # Edge case: Missing 'topic' in the request body
        response = await self.app.post(WORD_FREQUENCY_ENDPOINT, json={"n": 5})
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertIn("error", data)

        # Edge case: Missing 'n' in the request body
        response = await self.app.post(
            WORD_FREQUENCY_ENDPOINT, json={"topic": "Python"}
        )
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertIn("error", data)

        # Edge case: Invalid value for 'n' in the request body
        response = await self.app.post(
            WORD_FREQUENCY_ENDPOINT, json={"topic": "Python", "n": "abc"}
        )
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertIn("error", data)

    async def test_search_history_endpoint(self):

        response = await self.app.get(SEARCH_HISTORY_ENDPOINT)
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
        self.assertIn("topic", data[0])
        self.assertIn("top_words", data[0])


if __name__ == "__main__":
    unittest.main()
