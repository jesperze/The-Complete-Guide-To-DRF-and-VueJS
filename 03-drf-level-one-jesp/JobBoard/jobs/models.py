from django.db import models

class JobOffer(models.Model):
    company_name = models.CharField(max_length=50)
    company_email = models.CharField(max_length=120)
    job_title = models.CharField(max_length=200)
    job_description = models.CharField(max_length=200)
    salary = models.IntegerField()
    location = models.CharField(max_length=120)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{ self.author } { self.title }"
