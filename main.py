from PIL import Image
import os

INPUT_FOLDER = "images"
OUTPUT_FOLDER = "output"

TARGET_SIZE = (224, 224)

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

print("=" * 50)
print("IMAGE RESOLUTION POC")
print("=" * 50)

for image_name in os.listdir(INPUT_FOLDER):

    image_path = os.path.join(INPUT_FOLDER, image_name)

    image = Image.open(image_path)

    print(f"Image Name : {image_name}")
    print(f"Original Resolution : {image.size}")

    resized_image = image.resize(TARGET_SIZE)

    output_path = os.path.join(OUTPUT_FOLDER, image_name)

    resized_image.save(output_path)

    print(f"New Resolution : {TARGET_SIZE}")
    print("Status : Saved Successfully")

    print("-" * 40)