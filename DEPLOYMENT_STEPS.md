# 🚀 Deployment Steps for Finan Girls Fashion Market (Django + Railway)

## 1. Prerequisites
- Project code is pushed to GitHub.
- Railway account created: https://railway.app/

## 2. Create a Railway Project
- Go to Railway dashboard.
- Click **New Project** → **Deploy from GitHub repo**.
- Select your Django project repository.

## 3. Add PostgreSQL Plugin
- In Railway, click **Add Plugin** → **PostgreSQL**.
- Railway will create a database and set variables: `PGHOST`, `PGUSER`, `PGPASSWORD`, `PGDATABASE`, `PGPORT`.

## 4. Set Environment Variables
- In Railway, go to the **Variables** tab.
- Add all required variables (copy from `.env.example`):
  - `SECRET_KEY`
  - `DEBUG` (set to `False`)
  - `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`
  - `DEFAULT_FILE_STORAGE`
  - Map Railway’s DB variables:
    - `DB_NAME` = `PGDATABASE`
    - `DB_USER` = `PGUSER`
    - `DB_PASSWORD` = `PGPASSWORD`
    - `DB_HOST` = `PGHOST`
    - `DB_PORT` = `PGPORT`

## 5. Configure Django for Production
- In `config/settings.py`:
  - `ALLOWED_HOSTS = ['.railway.app', 'yourcustomdomain.com']`
  - `DEBUG = False`
- Static/media:
  - Use Cloudinary for media.
  - Run `python manage.py collectstatic` before deploy.

## 6. Add Procfile
- Already present:
  ```
  web: gunicorn config.wsgi
  ```

## 7. Push Code and Deploy
- Push your latest code to GitHub.
- Railway will auto-deploy on every push.

## 8. Run Migrations and Create Superuser
- In Railway’s shell or Deployments tab:
  - `python manage.py migrate`
  - `python manage.py createsuperuser`

## 9. Visit Your Live App
- Railway provides a `.railway.app` URL.
- Add a custom domain in Railway settings if needed.

## 10. Troubleshooting
- Check Railway logs for errors.
- Make sure all environment variables are set.
- For static/media issues, check Cloudinary and staticfiles settings.

---

**You’re ready to go! For any issues, check the Railway docs or ask for help.** 