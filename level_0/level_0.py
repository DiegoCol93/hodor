#!/usr/bin/python3
""" Module for storing the lvl-0 Post bot, for voting 1024 times. """
import requests


idN = '2219'
url = 'http://158.69.76.135/level0.php'

# Start a session.
s = requests.Session()

print("\033[92mLvl-0\033[0m, start voting.")

# Loop the requests
i = 0
while i < 1024:

    # Session post, with the id and the submit action.
    try:
        post = s.post(url, data={'id': idN, 'holdthedoor': 'submit'})
    except Exception as e:
        continue

    # Print post status.
    print("post: \033[92m{}\033[0m".format(post), end=' ')
    # Print page lenght.
    print("page-len: \033[92m{}\033[0m".format(len(post.text)))
    # Print vote #
    print("Vote #\033[92m{}\033[0m".format(i))
    print("\033[2;0f")  # Resets cursor.
    i += 1

print("Finished voting succesfully. \033[92m:)\033[0m")
