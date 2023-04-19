# Set your Cloudinary credentials
# ==============================
from dotenv import load_dotenv

load_dotenv()

# Import the Cloudinary libraries
# ==============================
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Import to format the JSON responses
# ==============================
import json

# Set configuration parameter: return "https" URLs by setting secure=True
# ==============================
config = cloudinary.config(secure=True)

# Log the configuration
# ==============================
# print(
#     "****1. Set up and configure the SDK:****\nCredentials: ",
#     config.cloud_name,
#     config.api_key,
#     "\n",
# )


def uploadImage(path_to_image: str) -> dict:
    # Upload the image and get its URL
    # ==============================

    # Upload the image.
    # Set the asset's public ID and allow overwriting the asset with new versions
    plant_image = cloudinary.uploader.upload(
        path_to_image,
        # unique_filename=False,
        overwrite=True,
        folder="PlantUrbanus",
    )

    # Build the URL for the image and save it in the variable 'srcURL'
    plant_public_id = plant_image["public_id"]
    srcURL = cloudinary.CloudinaryImage(plant_public_id).build_url()

    # Log the image URL to the console.
    # Copy this URL in a browser tab to generate the image on the fly.
    # print("****2. Upload an image****\nDelivery URL: ", srcURL, "\n")
    print(
        "****2. Upload an image****\nDelivery URL: ",
        srcURL,
        "\n",
        "Public Id: ",
        plant_public_id,
    )
    return {"public_id": plant_public_id, "uri": srcURL}


def getAssetInfo():
    # Get and use details of the image
    # ==============================

    # Get image details and save it in the variable 'image_info'.
    image_info = cloudinary.api.resource(plant_public_id)
    print(
        "****3. Get and use details of the image****\nUpload response:\n",
        json.dumps(image_info, indent=2),
        "\n",
    )

    # Assign tags to the uploaded image based on its width. Save the response to the update in the variable 'update_resp'.
    if image_info["width"] > 900:
        update_resp = cloudinary.api.update(plant_public_id, tags="large")
    elif image_info["width"] > 500:
        update_resp = cloudinary.api.update(plant_public_id, tags="medium")
    else:
        update_resp = cloudinary.api.update(plant_public_id, tags="small")

    # Log the new tag to the console.
    print("New tag: ", update_resp["tags"], "\n")


def createImageTag():
    # Transform the image
    # ==============================

    # Create an image tag with transformations applied to the src URL.
    imageTag = cloudinary.CloudinaryImage("coca-cola").image(
        radius="max", effect="sepia"
    )

    # Log the image tag to the console
    print("****4. Transform the image****\nTransfrmation URL: ", imageTag, "\n")


# def main():
#     uploadImage()
#     # getAssetInfo()
#     # createImageTag()


# main()
