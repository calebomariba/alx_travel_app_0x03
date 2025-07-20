# ALX Travel App

A Django-based travel listing platform designed to manage travel properties, bookings, and reviews with a RESTful API, MySQL database, and Swagger documentation.

## Project Overview

This project extends the foundation of a travel listing platform with API endpoints for managing listings and bookings, documented using Swagger.

## Task 0: Database Modeling and Data Seeding
- Defined models: `Listing`, `Booking`, and `Review` in `listings/models.py`.
- Created serializers for `Listing`, `Booking`, and `Review` in `listings/serializers.py`.
- Implemented a seeder command in `listings/management/commands/seed.py`.

## Task 1: API Development for Listings and Bookings

### Objectives
- Build API viewsets for `Listing` and `Booking` with CRUD operations.
- Configure RESTful endpoints under `/api/` using a router.
- Document endpoints with Swagger.

### Files
- `listings/views.py`: Contains `ListingViewSet` and `BookingViewSet` for CRUD operations.
- `listings/urls.py`: Configures API endpoints with a router.
- `alx_travel_app/urls.py`: Includes API and Swagger URLs.

### Setup Instructions
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/calebomariba/alx_travel_app_0x01.git
   cd alx_travel_app_0x01