from PIL import Image
import numpy as np
import os

INPUT_FOLDER = "images"
OUTPUT_FOLDER = "output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

print("=" * 70)
print("IMAGE NORMALIZATION POC")
print("=" * 70)

for image_name in os.listdir(INPUT_FOLDER):

    image_path = os.path.join(INPUT_FOLDER, image_name)

    if not os.path.isfile(image_path):
        continue

    try:

        image = Image.open(image_path).convert("RGB")

        image_array = np.array(image)

        print(f"\nImage : {image_name}")
        print(f"Before Normalization")
        print(f"Min Pixel : {image_array.min()}")
        print(f"Max Pixel : {image_array.max()}")

        normalized = image_array / 255.0

        print("\nAfter Normalization")
        print(f"Min Pixel : {normalized.min():.4f}")
        print(f"Max Pixel : {normalized.max():.4f}")

        normalized_image = (normalized * 255).astype(np.uint8)

        output_path = os.path.join(OUTPUT_FOLDER, image_name)

        Image.fromarray(normalized_image).save(output_path)

        print("Status : Success")
        print("-" * 70)

    except Exception as e:
        print(f"Error : {image_name}")
        print(e)