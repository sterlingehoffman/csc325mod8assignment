from django.test import TestCase
from django.urls import reverse


class PageViewTests(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1>Welcome to the Home Page!</h1>")

    def test_about_page(self):
        response = self.client.get(reverse("about"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1>About Page</h1>")
        self.assertContains(response, "<p>This is the about page of the website.</p>")
    def test_api_status(self):
        response = self.client.get(reverse("api_status"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")
