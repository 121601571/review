from django.db import models

# Create your models here.
class reviewModel(models.Model):
    reviewee_email = models.CharField(max_length=100)
    reviewer_email = models.CharField(max_length=100)
    rating = models.FloatField()
    comment = models.CharField(max_length=200)