from PIL import Image
import os

INPUT_FOLDER = "images"
OUTPUT_FOLDER = "output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

print("=" * 70)
print("COLOR SPACE CONVERSION POC")
print("=" * 70)

for image_name in os.listdir(INPUT_FOLDER):

    image_path = os.path.join(INPUT_FOLDER, image_name)

    if not os.path.isfile(image_path):
        continue

    try:

        image = Image.open(image_path)

        print(f"\nImage : {image_name}")
        print(f"Original Mode : {image.mode}")

        # Convert to RGB
        rgb_image = image.convert("RGB")

        # Convert to Grayscale
        gray_image = image.convert("L")

        filename = os.path.splitext(image_name)[0]

        rgb_path = os.path.join(
            OUTPUT_FOLDER,
            filename + "_rgb.jpg"
        )

        gray_path = os.path.join(
            OUTPUT_FOLDER,
            filename + "_gray.jpg"
        )

        rgb_image.save(rgb_path)
        gray_image.save(gray_path)

        print("RGB Image Saved")
        print("Grayscale Image Saved")
        print("-" * 70)

    except Exception as e:
        print(f"Error processing {image_name}")
        print(e)