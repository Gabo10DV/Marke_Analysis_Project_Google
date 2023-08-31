from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    category = models.JSONField()
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2)
    num_of_reviews = models.IntegerField()