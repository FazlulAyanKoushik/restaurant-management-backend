# Restaurant Management Backend
This Django backend provides functionality to manage restaurants and menus. It includes a custom user model with two types of users: owners and employees. The backend supports email and password authentication and includes an admin backend with search and filtering functionalities. APIs are available to create restaurants, join restaurants as employees, create menus, and list menus for owned restaurants. The APIs are permission-protected, meaning only users connected to a restaurant can access its menu.

# Installation
Clone the repository:

    git clone https://github.com/FazlulAyanKoushik/restaurant-management-backend.git

Install the required dependencies:

    pip install -r requirements.txt

Run the database migrations:

    python manage.py migrate

Create a superuser (admin) account:

    python manage.py createsuperuser

Start the development server:

    python manage.py runserver

The backend will be accessible at http://localhost:8000.

