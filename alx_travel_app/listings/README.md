# ALX Travel App

A Django-based travel listing platform designed to manage travel properties, bookings, and reviews with a RESTful API, MySQL database, and Swagger documentation.

## Project Overview

This project serves as a foundation for a scalable travel listing platform. It includes models for listings, bookings, and reviews, serializers for API representation, and a management command to seed the database with sample data.

## Task 0: Database Modeling and Data Seeding

### Objectives
- Define database models for `Listing`, `Booking`, and `Review`.
- Create serializers for `Listing` and `Booking` models.
- Implement a management command to seed the database with sample data.

### Files
- `listings/models.py`: Defines the `Listing`, `Booking`, and `Review` models.
- `listings/serializers.py`: Contains serializers for `Listing` and `Booking`.
- `listings/management/commands/seed.py`: Management command to populate the database.

### Setup Instructions
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/calebomariba/alx_travel_app_0x00.git
   cd alx_travel_app_0x00