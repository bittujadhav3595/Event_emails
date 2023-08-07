from django.test import TestCase
from django.core import mail
from django.utils import timezone
from .models import EmployeeEvent, EmailTemplate

class EventEmailTestCase(TestCase):
    def setUp(self):
        self.event_type = 'Birthday'
        self.employee_id = '001'
        self.event_date = timezone.now().date()
        EmployeeEvent.objects.create(
            event_type=self.event_type,
            employee_id=self.employee_id,
            date=self.event_date
        )
        EmailTemplate.objects.create(
            event_type=self.event_type,
            subject='Happy Birthday, {{name}}!',
            body='Dear {{name}},\n\nWishing you a fantastic birthday!'
        )

    def test_send_event_emails(self):
        response = self.client.post('/send-event-emails/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('Happy Birthday, 001!', mail.outbox[0].subject)
        self.assertIn('Dear 001,', mail.outbox[0].body)

