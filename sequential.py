import os
import time
from pipeline import process_image
from utils import get_image_paths

INPUT_DIR = 'data'
OUTPUT_DIR = 'output_sequential'

image_paths = get_image_paths(INPUT_DIR)

start = time.time()

for img_path in image_paths:
    rel_path = os.path.relpath(img_path, INPUT_DIR)
    output_path = os.path.join(OUTPUT_DIR, rel_path)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    process_image(img_path, output_path)

end = time.time()
print(f"Sequential Time: {end - start:.2f} seconds")