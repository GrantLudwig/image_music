import argparse
import cv2
import numpy
# import pygame
from pysinewave import SineWave
import time

low_pitch = -30
high_pitch = 20
color_range = 255
pitch_range = high_pitch - low_pitch

def calc_freq_from_color(color):
    return ((color * pitch_range) / color_range) + low_pitch

parser = argparse.ArgumentParser(description='image path')
parser.add_argument('image_path', type=str, help='The path to the image to make music out of')
args = parser.parse_args()

image = cv2.imread(args.image_path)
rows, cols, _ = image.shape

print('Playing song')

note_sound = SineWave(pitch = calc_freq_from_color(image[0, 0][0]), pitch_per_second = 100000)
note_sound2 = SineWave(pitch = calc_freq_from_color(image[0, 0][1]), pitch_per_second = 100000)
note_sound3 = SineWave(pitch = calc_freq_from_color(image[0, 0][2]), pitch_per_second = 100000)

note_sound.play()
note_sound2.play()
note_sound3.play()

for c in range(cols):
    for r in range(rows):
        note_sound.set_pitch(calc_freq_from_color(image[r, c][0]))
        note_sound2.set_pitch(calc_freq_from_color(image[r, c][1]))
        note_sound3.set_pitch(calc_freq_from_color(image[r, c][2]))
        time.sleep(0.0001)