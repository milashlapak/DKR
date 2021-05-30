from django.db import models

class VisitorRecord(models.Model):
    class Meta:
        unique_together = ['visitor_name', 'visitor_email', 'date']

    visitor_name = models.CharField(max_length=255)
    visitor_email = models.CharField(max_length=255)
    date = models.DateField()
