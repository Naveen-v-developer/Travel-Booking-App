# Travel Booking App

A simple Django web application for booking travel tickets (flight, train, bus).

## Features

- User registration, login, logout, profile management
- View and filter travel options
- Book tickets with seat selection
- Manage and cancel bookings
- Responsive Bootstrap 5 UI

## Setup Instructions

1. **Clone the repository**  
   `git clone <repo-url>`

2. **Install requirements**  
   `pip install -r requirements.txt`

3. **Configure MySQL database**  
   Edit `travel_booking_app/settings.py` with your MySQL credentials.

4. **Apply migrations**  
   `python manage.py migrate`

5. **Create superuser (optional)**  
   `python manage.py createsuperuser`

6. **Run the server**  
   `python manage.py runserver`

7. **Open your browser**  
   Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## MySQL Example Configuration

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'travel_booking_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## Running Tests

```
python manage.py test
```

## Deployment

- Use `python manage.py collectstatic` for static files.
- Set `DEBUG = False` and configure `ALLOWED_HOSTS` in `settings.py`.
- Use a production-ready WSGI server (e.g., Gunicorn, uWSGI).

