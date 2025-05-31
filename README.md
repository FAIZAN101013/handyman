# HandyMan Service Platform

A **Django-based platform** that connects customers with skilled **handyman service providers** for a range of home maintenance and repair needs.

[![Watch Demo](https://img.youtube.com/vi/N39ey6qDjQ8/0.jpg)](https://youtu.be/N39ey6qDjQ8)

---

## 🚀 Features

- 🔐 User Authentication (Customers & Providers)
- 👷 Service Provider Profiles with Ratings & Reviews
- 📅 Booking System for Services
- 📷 Image Uploads for Profiles & Listings
- 📱 Responsive & Modern UI
- ⭐ Rating and Review System

---

## 🧰 Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL (Production)
- **Media Storage**: AWS S3
- **Frontend**: HTML, CSS, JavaScript (Django Templates)
- **Deployment**: Heroku, AWS

---

## ✅ Prerequisites

- Python 3.11+
- PostgreSQL (for production)


---

## ⚙️ Local Development Setup

1. **Clone the repository:**
  
   git clone <repository-url>
   cd HandyMan
2. Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
  pip install -r requirements.txt

Create a .env file:
  cp .env.example .env


# Then edit the file with your environment-specific values
4. Apply migrations:
  python manage.py migrate

5. Create a superuser:
  python manage.py createsuperuser

6. Run the development server:
  python manage.py runserver
