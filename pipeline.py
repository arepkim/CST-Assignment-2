import cv2

from filters import (
    grayscale,
    gaussian_blur,
    sobel_edge,
    sharpen,
    adjust_brightness
)

def process_image(image_path, output_path):
    img = cv2.imread(image_path)
    
    gray = grayscale(img)
    blur = gaussian_blur(gray)
    edge = sobel_edge(blur)
    sharp = sharpen(edge)
    bright =adjust_brightness(sharp)

    cv2.imwrite(output_path, bright)