# 🚀 Deployment Steps for Finan Girls Fashion Market (Django + Render)

## 1. Prerequisites
- Project code is pushed to GitHub.
- Render account created: https://render.com/

## 2. Create a Render Web Service
- Go to the Render dashboard.
- Click **New Web Service** → **Connect your GitHub repo**.
- Select your Django project repository.

## 3. Add a PostgreSQL Database
- In Render, create a new **PostgreSQL** database from the dashboard.
- After creation, copy the `DATABASE_URL` provided by Render.

## 4. Set Environment Variables
- In your Render Web Service, go to the **Environment** tab.
- Add all required variables:
  - `SECRET_KEY`
  - `DEBUG` (set to `False`)
  - `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`
  - `DEFAULT_FILE_STORAGE` (optional, defaults to Cloudinary)
  - `DATABASE_URL` (paste from your Render PostgreSQL instance)
  - `ALLOWED_HOSTS` (optional, defaults to `.onrender.com,localhost,127.0.0.1`)

## 5. Configure Django for Production
- In `config/settings.py`:
  - `ALLOWED_HOSTS` includes `.onrender.com` (already set by default).
  - `DEBUG = False` (set via environment variable).
- Static/media:
  - Use Cloudinary for media.
  - Static files are handled by Whitenoise and/or Cloudinary.

## 6. Add Procfile
- Already present:
  ```
  web: gunicorn config.wsgi:application
  ```

## 7. Set Build and Start Commands
- **Build Command:**
  ```
  python manage.py migrate && python manage.py collectstatic --noinput
  ```
- **Start Command:**
  (from Procfile)
  ```
  gunicorn config.wsgi:application
  ```

## 8. Push Code and Deploy
- Push your latest code to GitHub.
- Render will auto-deploy on every push.

## 9. Run Migrations and Create Superuser
- In the Render Shell or via the Render dashboard:
  - `python manage.py migrate`
  - `python manage.py createsuperuser`

## 10. Visit Your Live App
- Render provides a `.onrender.com` URL.
- Add a custom domain in Render settings if needed.

## 11. Troubleshooting
- Check Render logs for errors.
- Make sure all environment variables are set.
- For static/media issues, check Cloudinary and staticfiles settings.

---

**You’re ready to go! For any issues, check the Render docs or ask for help.** 