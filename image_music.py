import argparse
import cv2
import numpy
import pygame

low_freq = 35
high = 10000
color_range = 255
freq_range = high - low_freq

def calc_freq_from_color(color):
    return ((color * freq_range) / color_range) + low_freq

parser = argparse.ArgumentParser(description='image path')
parser.add_argument('image_path', type=str, help='The path to the image to make music out of')
args = parser.parse_args()

image = cv2.imread(args.image_path)
rows, cols, _ = image.shape

# List BGR values left to right
#for c in range(cols):
#    for r in range(rows):
#        print(image[r, c])

# example code from: https://stackoverflow.com/questions/56592522/python-simple-audio-tone-generator
pygame.mixer.init(44100,-16,2,512)
sampleRate = 44100

sound_list = []


print('Generating song')
for c in range(cols):
    print('Column: ', c, 'of', cols)
    for r in range(rows):
        note_value = numpy.array([4096 * numpy.sin(2.0 * numpy.pi * calc_freq_from_color(image[r, c][0]) * x / sampleRate) for x in range(0, sampleRate)]).astype(numpy.int16)
        note = numpy.c_[note_value, note_value]
        note_sound = pygame.sndarray.make_sound(note)

        note_value2 = numpy.array([4096 * numpy.sin(2.0 * numpy.pi * calc_freq_from_color(image[r, c][1]) * x / sampleRate) for x in range(0, sampleRate)]).astype(numpy.int16)
        note3 = numpy.c_[note_value2, note_value2]
        note_sound2 = pygame.sndarray.make_sound(note3)

        note_value3 = numpy.array([4096 * numpy.sin(2.0 * numpy.pi * calc_freq_from_color(image[r, c][2]) * x / sampleRate) for x in range(0, sampleRate)]).astype(numpy.int16)
        note3 = numpy.c_[note_value3, note_value3]
        note_sound3 = pygame.sndarray.make_sound(note3)

        sound_list.append((note_sound, note_sound2, note_sound3))

for chord in sound_list:
    chord[0].play(-1)
    chord[1].play(-1)
    chord[2].play(-1)
    pygame.time.delay(500)
    note_sound.stop()
    note_sound2.stop()
    note_sound3.stop()