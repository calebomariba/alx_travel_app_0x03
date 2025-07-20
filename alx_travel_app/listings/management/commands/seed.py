from django.core.management import BaseCommand
from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
import random
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Seeds the database with sample data'

    def handle(self, *args, **options):
        # Clear existing data
        Listing.objects.all().delete()
        Booking.objects.all().delete()
        Review.objects.all().delete()

        # Sample data
        listings_data = [
            {'title': 'Cozy Beach House', 'description': 'A beautiful house by the beach', 'price_per_night': 150.00, 'location': 'Miami, FL'},
            {'title': 'Mountain Cabin', 'description': 'Quiet cabin in the mountains', 'price_per_night': 120.00, 'location': 'Aspen, CO'},
        ]

        # Create listings
        for data in listings_data:
            listing = Listing.objects.create(**data)
            self.stdout.write(self.style.SUCCESS(f'Created listing: {listing.title}'))

        # Create sample bookings
        listings = Listing.objects.all()
        for listing in listings:
            booking = Booking.objects.create(
                listing=listing,
                user_name=f'User{random.randint(1, 100)}',
                check_in=datetime.now().date() + timedelta(days=1),
                check_out=datetime.now().date() + timedelta(days=5),
                total_price=listing.price_per_night * 4
            )
            self.stdout.write(self.style.SUCCESS(f'Created booking for {listing.title}'))

        # Create sample reviews
        for listing in listings:
            review = Review.objects.create(
                listing=listing,
                user_name=f'User{random.randint(1, 100)}',
                rating=random.randint(1, 5),
                comment=f'Great stay at {listing.title}!'
            )
            self.stdout.write(self.style.SUCCESS(f'Created review for {listing.title}'))