from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Paulo Ricardo', cpf='12319162739',
                    email='paulo.pharmacia@hotmail.com', phone='21982256696')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]



    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'paulo.pharmacia@hotmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Paulo Ricardo',
            '12319162739',
            'paulo.pharmacia@hotmail.com',
            '21982256696'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

