from PIL import Image
import os

INPUT_FOLDER = "images"

print("=" * 70)
print("CORRUPTED IMAGE DETECTION POC")
print("=" * 70)

for image_name in os.listdir(INPUT_FOLDER):

    image_path = os.path.join(INPUT_FOLDER, image_name)

    if not os.path.isfile(image_path):
        continue

    print(f"\nImage : {image_name}")

    try:

        with Image.open(image_path) as image:
            image.verify()

        print("Status : VALID IMAGE")

    except Exception as e:

        print("Status : CORRUPTED IMAGE")
        print(f"Reason : {e}")

    print("-" * 70)