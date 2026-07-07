from PIL import Image
import os

INPUT_FOLDER = "images"
OUTPUT_FOLDER = "output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

print("=" * 70)
print("FILE FORMAT STANDARDIZATION POC")
print("=" * 70)

SUPPORTED_FORMATS = ["JPEG", "PNG", "WEBP", "BMP", "TIFF"]

for image_name in os.listdir(INPUT_FOLDER):

    image_path = os.path.join(INPUT_FOLDER, image_name)

    if not os.path.isfile(image_path):
        continue

    try:
        image = Image.open(image_path)

        print(f"\nImage : {image_name}")
        print(f"Original Format : {image.format}")

        rgb_image = image.convert("RGB")

        filename = os.path.splitext(image_name)[0]

        output_path = os.path.join(OUTPUT_FOLDER, filename + ".jpg")

        rgb_image.save(output_path, "JPEG", quality=95)

        print("Converted Format : JPEG")
        print("Status : Success")
        print("-" * 70)

    except Exception as e:
        print(f"Error processing {image_name}")
        print(e)