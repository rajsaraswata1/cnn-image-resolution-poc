import cv2
import os

INPUT_FOLDER = "images"

THRESHOLD = 500

print("=" * 70)
print("BLUR DETECTION POC")
print("=" * 70)

for image_name in os.listdir(INPUT_FOLDER):

    image_path = os.path.join(INPUT_FOLDER, image_name)

    if not os.path.isfile(image_path):
        continue

    image = cv2.imread(image_path)

    if image is None:
        continue

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur_score = cv2.Laplacian(gray, cv2.CV_64F).var()

    print(f"\nImage : {image_name}")
    print(f"Blur Score : {blur_score:.2f}")

    if blur_score < THRESHOLD:
        print("Status : BLUR IMAGE")
    else:
        print("Status : SHARP IMAGE")

    print("-" * 70)