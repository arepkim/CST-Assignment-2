import os

def get_image_paths(input_dir):
    image_paths = []
    for root, _, files in os.walk(input_dir):
        for f in files:
            if f.lower().endswith(('.jpg', '.png')):
                image_paths.append(os.path.join(root, f))
    return image_paths