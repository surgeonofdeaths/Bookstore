from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='will', email='will@email.com', password='testpass123'
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_super_user(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='superuser', email='superuser@gmail.com', password='testpass123'
        )
        self.assertEqual(user.username, 'superuser')
        self.assertEqual(user.email, 'superuser@gmail.com')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_superuser)















