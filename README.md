# Code For Fun

This repository contains my code scripts to automate boring stuff around me.

### `WhatsApp_img_notes_extractor`

Code to extract study notes from WhatsApp Images folder. I've trained a Convolutional Neural Network model to predict such images and extract them out of WhatsApp Images directory.

### `devrant.py` 

A Python script to send notifications when you hit a given number of "++"s on [devrant](devrant.com) (requires `BeautifulSoup`)

### `typeracer_plot.py`

A Python script to plot [typeracer](typeracer.com) speed statistics of a given user. (requires `Matplotlib` and `BeautifulSoup` )

### `auto_lan_auth`

A Python script to automate the LAN Authentication process on IIT (BHU) campus.

### `get_bhu_mails.py`

A python script to get the emails of all the professors of Banaras Hindu University.

Just run `get_bhu_mails.py` and it will crawl the contact section of BHU website, download all the docs containing details of every department, then use regex to get the emails out and paste it in results.txt.

### `csv_to_vcf.py`

A python script to create a VCF file using data (name and phone-number) stored in a CSV file.

### `hackerrank_medal.py`

A python script to know your medal in any Hackerrank contest.

### `set_router_ip.py`

A python script to reset IP of any Dlink router. The script will check for available IPs of the hostel, and it will use the given admin credentials to log in to the router admin portal, create a user session, and set the router IP to the one currently available :)

### `selenium/send.py`

A python script to send messages using WhatsApp web, using selenium.

### `selenium/gmail.py`

A python script to send emails using the Gmail web interface, using selenium.

Enjoy!