import unittest
from django.test import Client


class SimpleTest(unittest.TestCase):
    def test_details(self):
        client = Client()
        response = client.get("")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], "Hello, world!")


