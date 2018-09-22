# script to check for available github usernames

import requests

alphabet = 'abcdefghijklmnopqrstuvwxyz'
all_usernames = [x for x in alphabet]

for i, username in enumerate(all_usernames):
    res = requests.get('https://github.com/'+username)
    if res.status_code == 404:
        print(username)
    if not i % 100:
        print(i)
