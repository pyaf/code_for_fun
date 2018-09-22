import requests
import subprocess
from bs4 import BeautifulSoup

while True:
    url = "https://devrant.com/users/pyaf"
    response = requests.get(url)  # get html content
    soup = BeautifulSoup(response.text, "lxml")  # make a soup
    # parse the html to get score
    score = soup.find("div", class_="profile-score").get_text()
    if int(score[1:]) == 1000:
        # send notification of 1k ++s :)
        subprocess.call(
            ["notify-send", "-i", "", "Har har mahadev! 1k reached!"])
        break
    print("Current score:", score)  # print score to know current status
