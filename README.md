# 🧳 Travel Booking App

A simple Django web application for booking travel tickets (flight, train, bus).  

## ✨ Features

### 🔑 User Features
- User registration, login, logout, and profile management  
- View and filter travel options  
- Book tickets with seat selection  
- Manage and cancel bookings  
- Responsive Bootstrap 5 UI  

### 🛠️ Admin Features
- Manage **Travel Options** (add, edit, delete flights, trains, buses)  
- Manage **Users** (activate/deactivate accounts, update details)  
- Manage **Bookings** directly via Django Admin  

---

## ⚙️ Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone <repo-url>
   cd travel-booking-app
   ```

2. **Install requirements**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure MySQL database**  
   Edit `travel_booking_app/settings.py` with your MySQL credentials.  

4. **Apply migrations**  
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (for admin access)**  
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server**  
   ```bash
   python manage.py runserver
   ```

7. **Open your browser**  
   - App: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
   - Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  

---

## 🗄️ MySQL Example Configuration

```python
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

---

## 🧪 Running Tests

```bash
python manage.py test
```

---

## 🚀 Deployment

- Use `python manage.py collectstatic` for static files.  
- Set `DEBUG = False` and configure `ALLOWED_HOSTS` in `settings.py`.  
- Use a production-ready WSGI server (e.g., Gunicorn, uWSGI).  
- Can be deployed on **Render, Railway, PythonAnywhere, AWS, or Heroku**.  

---

## 🏆 Evaluation Criteria

- Backend functionality and Django best practices  
- Frontend design, usability, responsiveness  
- Code structure and quality  
- MySQL integration  
- Deployment (cloud readiness)  
- Problem-solving skills and creativity  
- Proper use of Django Admin for travel option & user management  
