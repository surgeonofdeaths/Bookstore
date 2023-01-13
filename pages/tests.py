from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView


class HomepageTests(SimpleTestCase):
    def setUp(self):
        self.response = self.client.get(reverse('home'))

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_correct_template_used(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_contain_text(self):
        self.assertContains(self.response, 'home page.')

    def test_doesnt_contain_text(self):
        self.assertNotContains(self.response, "this text shouldn't be here")

    def test_homepage_url_resolves_homepage_view(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)
        self.view = resolve(url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_correct_template_used(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_contains_correct_information(self):
        self.assertContains(self.response, 'About Page')
        self.assertNotContains(self.response, 'login page')

    def test_used_correct_view(self):
        self.assertEqual(self.view.func.__name__, AboutPageView.as_view().__name__)