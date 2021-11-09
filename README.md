# norobot
Простая графическая CAPTCHA, показывающая числа или слова вместо случайного набора букв.
Слова используются только безопасные - без негативной окраски.

Использование:
```
>>> import norobot
>>> norobot.gen_captcha()
{'image': <PIL.Image.Image image mode=RGB size=280x60 at 0x7F64A900E898>, 'word': 'мораль'}
```
Examples:

![example](https://github.com/SergeiMinaev/norobot/blob/master/examples/example_1.jpg)

![example](https://github.com/SergeiMinaev/norobot/blob/master/examples/example_2.jpg)

![example](https://github.com/SergeiMinaev/norobot/blob/master/examples/example_3.jpg)

![example](https://github.com/SergeiMinaev/norobot/blob/master/examples/example_5.jpg)

![example](https://github.com/SergeiMinaev/norobot/blob/master/examples/example_8.jpg)
