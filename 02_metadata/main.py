from PIL import Image
from PIL.ExifTags import TAGS
import os

INPUT_FOLDER = "images"

print("=" * 70)
print("IMAGE METADATA PREPROCESSING POC")
print("=" * 70)

IMPORTANT_TAGS = [
    "Make",
    "Model",
    "DateTime",
    "Orientation",
    "ImageWidth",
    "ImageLength",
    "Software",
    "XResolution",
    "YResolution",
]

for image_name in os.listdir(INPUT_FOLDER):

    image_path = os.path.join(INPUT_FOLDER, image_name)

    if not os.path.isfile(image_path):
        continue

    try:

        image = Image.open(image_path)

        print(f"\nImage : {image_name}\n")

        exif_data = image.getexif()

        if not exif_data:
            print("No EXIF Metadata Found")
            print("-" * 70)
            continue

        for tag_id, value in exif_data.items():

            tag = TAGS.get(tag_id, tag_id)

            if tag in IMPORTANT_TAGS:
                print(f"{tag} : {value}")

        print("-" * 70)

    except Exception as e:

        print(f"Error : {image_name}")
        print(e)