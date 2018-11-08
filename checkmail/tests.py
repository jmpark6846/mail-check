from django.test import TestCase
from django.urls import reverse

from checkmail.email import validate_email

# Create your tests here.
class MailValidationTestCase(TestCase):
    def setUp(self):
        self.mail = "jmpark6846@gmail.com"
        self.invalid_mail = "werj@wmeifow.co"

    def test_can_validate_a_correct_mail(self):
        res = self.client.get(reverse('checkmail:validate_mail', kwargs={'email':self.mail}))
        self.assertEqual(res.status_code, 200)

    def test_can_validate_an_incorrect_mail(self):
        res = self.client.get(reverse('checkmail:validate_mail', kwargs={'email':self.invalid_mail}))
        self.assertEqual(res.status_code, 400)
