#!/usr/bin/env python3

import random
from PIL import Image, ImageFont, ImageDraw, ImageEnhance, ImageOps


img_width = 280
img_height = 60
noise_color_range=(130,200)
word_color_range=(30,110)
letter_offset=30
words_file = "words_ru/words.txt"
fonts = ["fonts/betina-script-ctt.ttf", "fonts/sign-painter.otf"]
noise = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
noise_count = 60

with open(words_file) as f:
    lines = f.readlines()
    word = random.choice(lines)

img = Image.new('RGB', (img_width, img_height), (255, 255, 255))

n = 0
while n < noise_count:
    letter = random.choice(noise)
    letter_img = Image.new('L', (35,35))
    d = ImageDraw.Draw(letter_img)
    d.text((0,0),
            letter,
            font=ImageFont.truetype(random.choice(fonts), random.randrange(25,35)),
            fill=255)
    w = letter_img.rotate(random.randrange(1,190), expand=1)
    img.paste( ImageOps.colorize(w, (0,0,0),
            (random.randrange(noise_color_range[0],noise_color_range[1]),
                random.randrange(noise_color_range[0],noise_color_range[1]),
                random.randrange(noise_color_range[0],noise_color_range[1]))),
            (random.randrange(-30,img_width), random.randrange(-30,img_height)),  w)
    n += 1

offset = img_width / 2
offset = int(offset-(letter_offset*(len(word)/2))+5)
try:
    offset = random.randrange(5,offset)
except:
    pass

color = (random.randrange(word_color_range[0],word_color_range[1]),
        random.randrange(word_color_range[0],word_color_range[1]),
        random.randrange(word_color_range[0],word_color_range[1]))

for letter in word:
    letter = letter.upper()
    letter_img = Image.new('L', (50,50))
    d = ImageDraw.Draw(letter_img)
    d.text((3,3),
            letter,
            font=ImageFont.truetype(random.choice(fonts), 40),
            fill=255)
    w = letter_img.rotate(random.randrange(-30,30), expand=1)
    img.paste( ImageOps.colorize(w, color,color),
            (offset, random.randrange(1,10)),  w)
    offset += letter_offset
#img.save("out.jpg", "JPEG")
img.show()
