from rest_framework import serializers
from .models import Place

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields =  ['id','name','latitude','longitude','category','avg_rating','num_of_reviews']
        read_only_fields = ['id','name','latitude','longitude','category','avg_rating','num_of_reviews', ]