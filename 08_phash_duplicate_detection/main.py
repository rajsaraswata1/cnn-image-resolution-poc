from PIL import Image
import imagehash
import os

INPUT_FOLDER = "images"

print("=" * 70)
print("PERCEPTUAL HASH (pHash) DUPLICATE DETECTION POC")
print("=" * 70)

hashes = {}

for image_name in os.listdir(INPUT_FOLDER):

    image_path = os.path.join(INPUT_FOLDER, image_name)

    if not os.path.isfile(image_path):
        continue

    try:

        image = Image.open(image_path)

        phash = imagehash.phash(image)

        hashes[image_name] = phash

        print(f"{image_name} -> {phash}")

    except Exception as e:

        print(f"Error : {image_name}")
        print(e)

print("\n" + "=" * 70)
print("IMAGE SIMILARITY")
print("=" * 70)

files = list(hashes.keys())

for i in range(len(files)):
    for j in range(i + 1, len(files)):

        img1 = files[i]
        img2 = files[j]

        distance = hashes[img1] - hashes[img2]

        print(f"\n{img1}")
        print(f"{img2}")
        print(f"Hamming Distance : {distance}")

        if distance == 0:
            print("Status : EXACT DUPLICATE")

        elif distance <= 5:
            print("Status : VERY SIMILAR")

        elif distance <= 10:
            print("Status : SIMILAR")

        else:
            print("Status : DIFFERENT")

        print("-" * 70)