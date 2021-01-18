#!/usr/bin/python3
""" Module for storing the lvl-3 Post bot, for voting 1024 times. """
import requests
from PIL import Image
import pytesseract
from io import BytesIO
import sys

idN = '2219'
url = 'http://158.69.76.135/level3.php'
header = {'User-Agent':
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML'
          + ', like Gecko) Chrome/83.0.4103.9 Safari/537.36',
          'Referer': url}
img_Link = 'http://158.69.76.135/captcha.php'

# Start a session.
s = requests.Session()

print("\033[92mLvl-3\033[0m, start voting.")

# Loop the requests
i = 0
while i < 1024:

    print("Get page: ", end='')
    page = s.get(url)
    print("\033[92m{}\033[0m".format(page))

    print("Get img: ", end='')
    img = s.get(img_Link)
    print("\033[92m{}\033[0m".format(img))

    img_open = Image.open(BytesIO(img.content))
    img_open.convert('L')
    img_open = img_open.point(lambda x: 0 if x < 143 else 255)
    img_open.save("captcha2.png")
    captcha_str = pytesseract.image_to_string(img_open).strip()
    print("OCR Got: \033[92m{}\033[0m".format(captcha_str))

    print("Get cookie: ", end='')
    cookie = page.cookies['HoldTheDoor']
    print("\033[92m{}\033[0m".format(cookie))

    # Session post, with the id and the submit action.
    try:
        post = s.post(url,
                      data={'id': idN, 'holdthedoor': 'submit', 'key': cookie,
                            'captcha': captcha_str},
                      cookies={'HoldTheDoor': cookie},
                      headers=header)
    except Exception as e:
        continue

    # Print post status.
    print("post: \033[92m{}\033[0m".format(post), end=' ')
    # If wrong page.
    if len(post.text) < 1024:
        print("page-len: \033[91m{}\033[0m".format(len(post.text)))
        print("\033[2;0f")  # Resets cursor.
        continue
    # Print page lenght.
    print("page-len: \033[92m{}\033[0m".format(len(post.text)))
    # Print vote #
    print("Vote #\033[92m{}\033[0m".format(i))
    print("\033[2;0f")  # Resets cursor.
    i += 1

print("\033[7;0f")  # Sets cursor for end.
print("Finished voting succesfully. \033[92m:D\033[0m")
