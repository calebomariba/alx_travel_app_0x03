from rest_framework import serializers
from .models import Listing, Booking, Review

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
       

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
       