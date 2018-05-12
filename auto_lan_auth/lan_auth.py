import requests
from lxml import html
from bs4 import BeautifulSoup

# set your username and password here
username = ''
password = ''

def crawl():
    session_requests = requests.session()
    url = 'http://www.msftncsi.com/ncsi.txt' # a light weight webpage
    result = session_requests.get(url)
    
    # check if already authenticated
    if 'Microsoft' in result.text:
        print('Already Authenticated!')
        return

    # extract hidden form token
    tree = html.fromstring(result.text)
    auth_token = list(set(tree.xpath("//input[@name='magic']/@value")))[0]

    # prepare payload for form submission
    payload = {
        "4Tredir":'',
        "username": username, 
        "password": password, 
        "magic": auth_token,
    }
    # submit the authentication form
    resp = session_requests.post(
            'http://192.168.249.1:1000/', 
            data = payload, 
            headers = dict(referer=url)
        )
    
    # parse the response
    if 'Firewall authentication failed. Please try again.' in resp.text:
        print('Authentication Failure, Please check your username and password.')
    if 'Firewall Authentication Keepalive Window' in resp.text:
        print('Authentication Successful, Enjoy!')

crawl()
