import argparse
import cv2
import numpy

parser = argparse.ArgumentParser(description='image path')
parser.add_argument('image_path', type=str, help='The path to the image to make music out of')
args = parser.parse_args()

image = cv2.imread(args.image_path)
print(image)
rows, cols, _ = image.shape

# List BGR values left to right
for c in range(cols):
    for r in range(rows):
        print(image[r, c])