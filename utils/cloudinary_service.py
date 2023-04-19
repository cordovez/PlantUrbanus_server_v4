# Set your Cloudinary credentials
# ==============================
import os
import pathlib
import cloudinary.api
import cloudinary.uploader
import cloudinary
from dotenv import load_dotenv, dotenv_values

load_dotenv()

env = dotenv_values(".env")

config = cloudinary.config(
    secure=True,
    cloud_name=env["CLOUD_NAME"],
    api_key=env["API_KEY"],
    api_secret=env["API_SECRET"],
)

supported_files = (".jpg", ".jpeg", ".png", ".heic")
# Log the configuration
# ==============================
print(
    "****1. Set up and configure the SDK:****\nCredentials: ",
    config.cloud_name,
    config.api_key,
    "\n",
)


def upload_image(filename, folder="PlantUrbanus"):
    stem = pathlib.Path(filename).stem
    res = cloudinary.uploader.upload(filename, folder=folder)
    #     res = cloudinary.uploader.upload(filename, public_id=stem, folder=folder)
    return res


def upload_and_tag_image(filename, folder="PlantUrbanus"):
    stem = pathlib.Path(filename).stem
    res = cloudinary.uploader.upload(
        filename, folder=folder, detection="openimages", auto_tagging=0.25
    )
    return res


def upload_folder():
    n = 0
    for file in sorted(os.listdir("photos")):
        if pathlib.Path(file).suffix.lower() in supported_files:
            try:
                upload_and_tag_image("photos/" + file)
                n += 1
            except Exception as e:
                print("failed", file)
                print(e)

    print(n, "photos uploaded")


# res = upload_and_tag_image('Jane.jpg')
# print(res)
upload_folder()
