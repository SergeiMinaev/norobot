#!/usr/bin/env python3
import os
import random
from PIL import Image, ImageFont, ImageDraw, ImageEnhance, ImageOps


BASE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)))

img_width = 300
img_height = 60
noise_color_range = (140,200)
word_color_range = (30,100)
word_font_size = 45
letter_offset = 33
words_file = os.path.join(BASE_DIR, "words_ru/words.txt")
fonts = [
    "fonts/betina-script-ctt.ttf",
    "fonts/sign-painter.otf"
]
noise = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
noise_count = 60
noise_font_size_range = (35,40)


def gen_captcha(width = img_width, just_numbers = False):
    if just_numbers:
        word = str(random.randint(100000,999999))
    else:
        with open(words_file) as f:
            lines = f.readlines()
            word = random.choice(lines)
            word = word.replace('\n', '')

    img = Image.new('RGB', (img_width, img_height), (255, 255, 255))

    n = 0
    while n < noise_count:
        letter = random.choice(noise)
        letter_img = Image.new('L', (35,35))
        d = ImageDraw.Draw(letter_img)
        d.text((0,0),
                letter,
                font=ImageFont.truetype(
                    os.path.join(BASE_DIR, random.choice(fonts)),
                    random.randrange(noise_font_size_range[0],noise_font_size_range[1])),
                fill=255)
        w = letter_img.rotate(random.randrange(1,190), expand=1)
        img.paste( ImageOps.colorize(w, (0,0,0),
                (random.randrange(noise_color_range[0],noise_color_range[1]),
                    random.randrange(noise_color_range[0],noise_color_range[1]),
                    random.randrange(noise_color_range[0],noise_color_range[1]))),
                (random.randrange(-30,img_width), random.randrange(-30,img_height)),  w)
        n += 1

    offset = img_width / 2
    offset = int(offset-(letter_offset*(len(word)/2))+2)
    try:
        offset = random.randrange(2,offset)
    except:
        pass

    color = (random.randrange(word_color_range[0],word_color_range[1]),
            random.randrange(word_color_range[0],word_color_range[1]),
            random.randrange(word_color_range[0],word_color_range[1]))

    for letter in word:
        letter = letter.upper()
        letter_img = Image.new('L', (int(word_font_size*1.2), int(word_font_size*1.2)))
        d = ImageDraw.Draw(letter_img)
        if letter == '7': font = fonts[0]
        elif letter == '1': font = fonts[1]
        else: font = random.choice(fonts)
        d.text((3,3),
                letter,
                font=ImageFont.truetype(
                    os.path.join(BASE_DIR, font),
                    word_font_size),
                fill=255)
        w = letter_img.rotate(random.randrange(-30,30), expand=1)
        img.paste( ImageOps.colorize(w, color,color),
                (offset, random.randrange(-1,3)),  w)
        offset += letter_offset
    img = img.resize((width, int(width * img_height / img_width)), Image.ANTIALIAS)
    return {'img': img, 'secret': word}
