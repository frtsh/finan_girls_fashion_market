# Finan Girls Fashion Market

A modern e-commerce platform for fashion products, built with Django. Easily deployable to Railway with PostgreSQL and Cloudinary support.

## Features
- User registration, login, and profile management
- Product catalog with categories and reviews
- Blog for announcements and trends
- Image hosting via Cloudinary
- Admin dashboard
- Responsive design

## Tech Stack
- Python 3
- Django
- PostgreSQL
- Cloudinary (media storage)
- Railway (deployment)

## Local Setup

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd finan_girls_fashion_market
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On Mac/Linux
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set up environment variables:**
   - Copy `.env.example` to `.env` and fill in required values (SECRET_KEY, DB settings, Cloudinary, etc.)
5. **Apply migrations and load sample data:**
   ```sh
   python manage.py migrate
   python manage.py loaddata products/products_fixture.json  # Optional: load sample products
   ```
6. **Create a superuser:**
   ```sh
   python manage.py createsuperuser
   ```
7. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

## Deployment on Railway

1. Push your code to GitHub.
2. Create a new project on [Railway](https://railway.app/), connect your repo.
3. Add the PostgreSQL plugin and map DB variables as described in `DEPLOYMENT_STEPS.md`.
4. Set all required environment variables (see `.env.example`).
5. Add a `Procfile` with:
   ```
   web: gunicorn config.wsgi
   ```
6. Deploy! Railway will build and run your app automatically.
7. Run migrations and create a superuser from the Railway shell:
   ```sh
   python manage.py migrate
   python manage.py createsuperuser
   ```

## Usage
- Visit `/` for the product catalog
- `/blog/` for blog posts
- `/admin/` for admin dashboard
- `/accounts/` for user authentication

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENSE) 