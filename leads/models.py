from django.db import models

from accounts.models import User

class Lead(models.Model):

    STATUS_CHOICES = [
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Interested', 'Interested'),
        ('Converted', 'Converted'),
        ('Lost', 'Lost'),
    ]

    SOURCE_CHOICES = [
        ('Website', 'Website'),
        ('Social Media', 'Social Media'),
        ('Referral', 'Referral'),
        ('Advertisement', 'Advertisement'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    company = models.CharField(max_length=100, null=True, blank=True)

    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')

    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name