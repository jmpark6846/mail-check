from django.test import TestCase
from django.urls import reverse

from mymail.email import validate_email

# Create your tests here.
class MailValidationTestCase(TestCase):
    def setUp(self):
        self.mail = "jmpark6846@gmail.com"
        self.invalid_mail = "werj@wmeifow.co"

    def test_can_validate_an_mail(self):
        mail_data = { 'email': self.mail }
        res = self.client.post(reverse('mymail:validate_email'), mail_data)
        self.assertEqual(res.status_code, 200)
