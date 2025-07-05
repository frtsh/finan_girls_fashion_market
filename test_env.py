from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")
print("Cloud Name:", os.getenv("CLOUDINARY_CLOUD_NAME"))
print("API Key:", os.getenv("CLOUDINARY_API_KEY"))
print("API Secret:", os.getenv("CLOUDINARY_API_SECRET")) 