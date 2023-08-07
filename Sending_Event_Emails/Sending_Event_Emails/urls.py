from django.urls import path
from EventEmails.views import send_event_emails

urlpatterns = [
    path('send-event-emails/', send_event_emails, name='send_event_emails')
    # Add other URLs for your project if needed
]

