from django.test import TestCase
from books.models import Book, Review
from django.urls import reverse
from django.contrib.auth import get_user_model


class BookTests(TestCase):
    # setUp - runs before every single test
    # setUpTestData - runs just once
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Harry Potter",
            author="JK Rowling",
            price="25.00",
        )
        cls.user = get_user_model().objects.create_user(
            username="reviewuser",
            email="reviewuser@email.com",
            password="testpass123",

        )
        cls.review = Review.objects.create(
            book=cls.book,
            review="An excellent review",
            author=cls.user,
        )

    def test_book_listing(self):
        self.assertEqual(self.book.title, "Harry Potter")
        self.assertEqual(self.book.author, "JK Rowling")
        self.assertEqual(self.book.price, "25.00")

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Harry Potter")
        self.assertContains(response, 'An excellent review')
        self.assertTemplateUsed(response, 'books/book_detail.html')
