from django.db import models

class EmployeeEvent(models.Model):
    EVENT_TYPES = (
        ('Birthday', 'Birthday'),
        ('Work Anniversary', 'Work Anniversary'),
        # Add more event types here if needed
    )

    employee_id = models.CharField(max_length=10)
    event_type = models.CharField(choices=EVENT_TYPES, max_length=20)
    date = models.DateField()
