# HandyMan Service Platform

A Django-based platform for connecting customers with handyman service providers.

## Features

- User authentication (customers and service providers)
- Service provider profiles with ratings and reviews
- Service booking system
- Image upload for profiles and services
- Responsive modern UI
- Rating and review system

## Prerequisites

- Python 3.11+
- PostgreSQL (for production)
- AWS S3 bucket (for media storage in production)

## Local Development Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd HandyMan
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file:
```bash
cp .env.example .env
# Edit .env with your settings
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## Production Deployment

### Heroku Deployment

1. Install Heroku CLI and login:
```bash
heroku login
```

2. Create a new Heroku app:
```bash
heroku create your-app-name
```

3. Add PostgreSQL addon:
```bash
heroku addons:create heroku-postgresql:hobby-dev
```

4. Configure environment variables:
```bash
heroku config:set DJANGO_SECRET_KEY=your-secret-key
heroku config:set DJANGO_DEBUG=False
heroku config:set DJANGO_ALLOWED_HOSTS=your-app-name.herokuapp.com
heroku config:set USE_AWS=True
heroku config:set AWS_ACCESS_KEY_ID=your-aws-key
heroku config:set AWS_SECRET_ACCESS_KEY=your-aws-secret
heroku config:set AWS_STORAGE_BUCKET_NAME=your-bucket-name
```

5. Deploy:
```bash
git push heroku main
```

6. Run migrations:
```bash
heroku run python manage.py migrate
```

7. Create superuser:
```bash
heroku run python manage.py createsuperuser
```

### AWS S3 Setup

1. Create an S3 bucket in AWS
2. Configure CORS on the bucket
3. Create an IAM user with S3 access
4. Add the AWS credentials to your environment variables

## Environment Variables

See `.env.example` for required environment variables.

## Security Considerations

- Always use HTTPS in production
- Keep your SECRET_KEY secure
- Enable AWS S3 bucket encryption
- Regular security updates
- Database backups

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License. 