Title: Breaking the NY State Tax Return Captcha with Python and Tesseract
Author: Peter Downs
Date: Wednesday, March 3, 2016

Earlier today I went online to check the status of my tax return refund. (Yes, I take the appropriate withholding allowances. It's unbelievable to me how online commenters are quick to roast people for "giving the government a free loan" without understanding anything of their tax situation.) It turns out that unlike the California or Federal systems, [the New York State tax refund procedure](https://www8.tax.ny.gov/PRIS/prisStart) requires you to fill out a captcha before going anywhere. Not just any captcha – check out this beauty:

![ny state captcha][1]

[1]: /static/img/ny-captcha-enlarged.jpg "OK, I 'enhanced' it a little bit"

It never occurred to me to try to break a captcha before but this looked like the easiest possible target. Five minutes later I was done. Three of those minutes involved setting up dependencies: [Tesseract](https://github.com/tesseract-ocr/tesseract), [Pytesseract](https://github.com/madmaze/pytesseract), and [Pillow](http://python-pillow.org). Thanks to modern packaging tools (thanks, [brew](http://brew.sh) and [wheel](http://pythonwheels.com)) this was painless and fast.

```bash
$ brew install tesseract
$ pip install pytesseract pillow
```

(OK, I actually created a new directory and
[virtualenv](https://virtualenv.pypa.io/en/latest/) for this, just like I do
with all of my projects, but you get the idea.)

Breaking the captcha was then as easy as saving it (as `captcha.jpg`) and
running the following python code:

```python
import pytesseract as tes
from PIL import Image

img = Image.open('captcha.jpg')
print 'captcha =', tes.image_to_string(img)
```

```bash
$ python ocr.py
captcha = 740120
```

Two logical steps – kind of incredible. Further proof that there's no point in
using a captcha if [it isn't made by Google](https://googleonlinesecurity.blogspot.com/2014/12/are-you-robot-introducing-no-captcha.html). Sure, [older versions of captcha were
susceptible to automated
humans](http://www.troyhunt.com/2012/01/breaking-captcha-with-automated-humans.html), but how can you defeat _ARTIFICIAL INTELLIGENCE_?
