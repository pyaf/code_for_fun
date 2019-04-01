###########################################################
## Scipt to plot speed stats of any typeracer user
###########################################################

import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

username = "agga_daku"  # typeracer username
num_races = 1000  # number of last races to plot, too high value may result in error :/
url = "https://data.typeracer.com/pit/race_history?user=%s&n=%s&startDate=" % (username, num_races)

response = requests.get(url)  # get html content
soup = BeautifulSoup(response.text, "lxml")  # make a soup
speed_data = []
for row in soup.find('table', class_="scoresTable").findAll('tr'):
    try:
        speed_data.append(int(row.findAll('td')[1].contents[0].split(' ')[0]))
    except:
        pass
speed_data = list(reversed(speed_data))
# plot using matplotlib
plt.plot(range(len(speed_data)), speed_data)
plt.show()
