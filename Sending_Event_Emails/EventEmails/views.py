from django.core.mail import send_mail
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import EmployeeEvent, EmailTemplate

@csrf_exempt
def send_event_emails(request):
    if request.method == 'POST':
        today = timezone.now().date()
        events_today = EmployeeEvent.objects.filter(date=today)

        for event in events_today:
            email_template = EmailTemplate.objects.get(event_type=event.event_type)
            subject = email_template.subject.replace('{{name}}', event.employee_id)
            body = email_template.body.replace('{{name}}', event.employee_id)



            send_mail(
                subject=subject,
                message=body,
                from_email='sender@example.com',
                recipient_list=[event.employee_id + '@example.com'],
                fail_silently=False,
            )

        return JsonResponse({'message': 'Event emails sent successfully.'})
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)

