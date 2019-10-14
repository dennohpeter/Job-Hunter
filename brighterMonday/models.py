from django.db import models
from django.utils import timezone

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    job_function = models.CharField(max_length=100, null=True)
    company_logo = models.URLField(max_length=200, null=True)
    company_logo_alt = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=50)
    location =models.CharField(max_length=50)
    employer = models.CharField(max_length=50)
    more_info_link = models.URLField(max_length=200)
    salary = models.CharField(max_length=50)
    job_type = models.CharField(max_length=50)
    first_seen = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    summary_title = models.CharField(max_length=100, null=True)
    summary = models.TextField(null=True)
    description_title = models.CharField(max_length=100, null=True)
    requirements = models.TextField(null=True)
    
    


    def __str__(self):
        """ Return a human readable representation of model instance"""
        return self.title
