# User Management Project

This project is a Django-based application for managing user access to different services based on their roles and permissions. It includes API endpoints to handle user-specific requests for hotel and flight bookings.

*Date:* January 9, 2025  
*Author:* Sarath S  
*Email:* sarathsurendhran10@gmail.com

## Prerequisites

Before running the project, ensure you have the following installed:

- Django 
- Python 3.10+
- Django REST Framework

## Installation

1. Clone the repository:
   bash
   git clone https://github.com/Sarathsurendhran/user_manage_system.git
   cd user-management
   

2. Install the required dependencies:
   bash
   pip install -r requirements.txt
   

3. Apply migrations:
   bash
   python manage.py migrate
   

4. Start the development server:
   bash
   python manage.py runserver
   

## URL Endpoints

### ProtectedView Endpoints
These endpoints are for premium users to access hotel and flight booking services.

- GET /hotel-booking/<int:id>/
- GET /flight-booking/<int:id>/

*Response:*
- Status 200: "access granted"
- Status 401: "you do not have permission"

### RoleView Endpoints
These endpoints check user roles for assistant services related to hotel and flight bookings.

- GET /assistant-hotel-booking/<int:id>/
- GET /assistant-flight-booking/<int:id>/

*Response:*
- Status 200: "access granted"
- Status 404: Not Found

## Views


## License

This project is licensed under the MIT License. See the LICENSE file for details.