from django.test import TestCase


class TestMain(TestCase):
    def test_view1(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
