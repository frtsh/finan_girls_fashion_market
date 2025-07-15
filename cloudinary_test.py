import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(dotenv_path=".env")
print("Cloud Name:", os.getenv("CLOUDINARY_CLOUD_NAME"))
print("API Key:", os.getenv("CLOUDINARY_API_KEY"))
print("API Secret:", os.getenv("CLOUDINARY_API_SECRET"))

# Configuration
cloudinary.config(
  cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME"),
  api_key = os.getenv("CLOUDINARY_API_KEY"),
  api_secret = os.getenv("CLOUDINARY_API_SECRET"),
  secure=True
)

# Upload an image
upload_result = cloudinary.uploader.upload("", public_id="shoes")
print(upload_result["secure_url"])

# Optimize delivery
optimize_url, _ = cloudinary_url("shoes", fetch_format="auto", quality="auto")
print(optimize_url)

# Transform the image
auto_crop_url, _ = cloudinary_url("shoes", width=500, height=500, crop="auto", gravity="auto")
print(auto_crop_url)

#python manage.py loaddata products/products_fixture.json