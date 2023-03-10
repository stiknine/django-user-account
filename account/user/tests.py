import random
import secrets
import string

from django.test import TestCase
from django.urls import reverse

from .models import Account
from .forms import AccountCreateForm


class AccountModelTest(TestCase):
    username = ''
    email = ''

    @classmethod
    def setUpTestData(cls):
        """Create new user account."""
        cls.username = 'test' + random.choice(string.digits)
        cls.email = f'{cls.username}@test.com'
        password = secrets.token_urlsafe(8)
        cls.user_account = Account.objects.create_user(cls.username, cls.email, password)

    def test_username_created(self):
        """Test username was created for the user account."""
        self.assertEqual(self.user_account.username, self.username)

    def test_email_created(self):
        """Test email was created for the user account."""
        self.assertEqual(self.user_account.email, self.email)

    def test_user_account_str_rep(self):
        """Test user account __str__ method."""
        self.assertEqual(str(self.user_account), self.username)

    def test_email_unique(self):
        """Test email is a unique field."""
        email_unique = self.user_account._meta.get_field('email').unique
        self.assertIs(email_unique, True)


class AccountViewTest(TestCase):
    username = ''
    email = ''
    password = ''

    @classmethod
    def setUpTestData(cls):
        """Create new user account, so we can test user login."""
        cls.username = 'test' + random.choice(string.digits)
        cls.password = secrets.token_urlsafe(8)
        cls.email = f'{cls.username}@test.com'
        cls.user_account = Account.objects.create_user(cls.username, cls.email, cls.password)

    def test_index_location(self):
        """Test index view location."""
        response = self.client.get('/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_index_name_and_template(self):
        """Test index view name and correct template."""
        response = self.client.get(reverse('user:index'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_register_location(self):
        """Test register view location."""
        response = self.client.get('register/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_register_name_and_template(self):
        """Test register view name and correct template."""
        response = self.client.get(reverse('user:register'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_login_location(self):
        """Test login view location."""
        response = self.client.get('login/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_login_name_and_template(self):
        """Test login view name and correct template."""
        response = self.client.get(reverse('login'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_and_home(self):
        """Test user login and home."""
        login = self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('user:home'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'Welcome home, <strong>{self.username}</strong>!')
        self.assertTemplateUsed(response, 'home.html')

    def test_account_register(self):
        """Test user account registration."""
        response = self.client.post(reverse('user:register'),
                                    data={'username': self.username,
                                          'email': self.email,
                                          'password1': self.password,
                                          'password2': self.password})
        self.assertEqual(response.status_code, 301)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('user:home'), follow=True)
        self.assertRedirects(response, '/login/?next=/home/', status_code=301)


class AccountFormTest(TestCase):
    def test_register_form_username_help_text(self):
        """Test username help text."""
        form = AccountCreateForm()
        self.assertEqual(form.fields['username'].help_text, '4 to 150 characters. Letters, numbers and @ . + - _ only.')

    def test_register_form_username_min_length(self):
        """Test username minimum length validation."""
        form = AccountCreateForm(data={'username': 'abc', 'email': '', 'password1': '', 'password2': ''})
        self.assertFalse(form.is_valid())
        self.assertIn("Enter a valid username, must be a minimum of 4 characters.", form.errors['username'])
