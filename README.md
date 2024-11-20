# Handy Man

A **Django platform** that connects customers with local handymen — search by
service or postcode, book a pro, and track the job from request to review.

[![Watch Demo](https://img.youtube.com/vi/N39ey6qDjQ8/0.jpg)](https://youtu.be/N39ey6qDjQ8)

---

## Features

**For customers**
- 🔍 Search handymen by service, keyword, or postcode, with price and rating filters
- 📅 Book with a task description, date, time, and photo — with a live price estimate
- 📬 Email notifications when a handyman accepts or declines
- 🗂 My Bookings with status tracking (pending / accepted / completed) and full-detail popups
- ⭐ Rate and review handymen after the job is done

**For handymen (FixRs)**
- 📊 Dashboard with incoming requests, rating, review count, and jobs completed
- 💡 Profile suggestions that show exactly what to add to win more bookings
- ✅ Accept / decline requests, manage approved jobs, mark work complete
- 👤 Profile with photo, bio, services, tags, and hourly rate

**Platform**
- 🔐 Role-based access — workers and customers each see only their own flow
- 🎨 Responsive Bootstrap 5 UI with a shared design system
- ✉️ Full password-reset flow via email

## Tech Stack

- **Backend:** Django 4.2, custom user model with role flags
- **Frontend:** Django templates, Bootstrap 5, vanilla JS
- **Database:** SQLite for development, PostgreSQL-ready via `DATABASE_URL`
- **Deployment:** Gunicorn + WhiteNoise (Procfile included)

## Local Setup

1. **Clone and enter the project**

   ```bash
   git clone https://github.com/FAIZAN101013/handyman.git
   cd handyman
   ```

2. **Create a virtual environment and install dependencies**

   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   # source venv/bin/activate   # macOS / Linux
   pip install -r requirements.txt
   ```

3. **Configure the environment**

   ```bash
   copy .env.example .env       # Windows (cp on macOS/Linux)
   ```

   Then edit `.env` — at minimum set `DJANGO_SECRET_KEY` (generate one with
   `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`).
   With `DJANGO_DEBUG=True`, outgoing email prints to the console; for real
   email, set `EMAIL_HOST_USER` and a Gmail **App Password**.

4. **Migrate and run**

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

   Open http://127.0.0.1:8000/ — sign up as a customer ("I want to hire"),
   a handyman ("I want to work"), or both.

## Project Structure

```
handyman/
├── Kwic_FixR_Main/      # Project settings, URLs, WSGI
├── userhandle/          # App: models, views, forms, templates
│   ├── templates/       # All pages (extend base.html)
│   └── serviceview.py   # Service browse & filter views
├── static/style/hm.css  # Design system
├── .env.example         # Environment template — copy to .env
└── Procfile             # Gunicorn entry point for deployment
```
