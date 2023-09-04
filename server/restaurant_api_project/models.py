from django.db import models

class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256, blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    review_count = models.IntegerField()
    categories = models.CharField(max_length=256)

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    registration_date = models.DateField()

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True)
    text = models.TextField(null=True)
    time = models.DateField()
