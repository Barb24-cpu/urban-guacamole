import os
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)

def upload_image_to_cloudinary(file_stream, folder: str = "products") -> dict:
    """
    Uploads a file stream or bytes to Cloudinary.
    """
    try:
        response = cloudinary.uploader.upload(file_stream, folder=folder)
        return response
    except Exception as e:
        raise RuntimeError(f"Cloudinary upload failed: {str(e)}")

# Alias so both function names work if imported elsewhere
upload_to_cloud = upload_image_to_cloudinary