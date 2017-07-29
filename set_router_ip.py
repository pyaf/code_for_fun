import os
import requests
import time

#Check which IPs are available
i = 2
while i!=254:
    IP = "10.9.1.%d" %i #example
    response = os.system("ping -c 1 " + IP)
    print(response)

    if response == 0:
        print(IP, 'is not available!')
    else:
        print('\n\n Gotchha!')
        print(IP, 'is down!')
        print('Gonna use this IP for your router!')
        break
    i+=1

print('Logging In')
os.environ['NO_PROXY'] = '192.168.0.1'
del os.environ['http_proxy']
del os.environ['https_proxy']

session_requests = requests.session()
# session_requests.trust_env = False
login_url = 'http://192.168.0.1/login.cgi'
login_payload = {
    'username': '<your username>',
    'password': '<your password>',
    'submit.htm?login.htm': 'Send'
}

session_requests.post(
    login_url,
    data = login_payload,
    headers = dict(referer=login_url)
)

print('Logged In\nSession created')
final_payload = {
    'save':'Apply Changes',
    'staip_gateway' :'10.9.1.1',
    'staip_ipaddr' :IP,
    'staip_mtusize' :'1500',
    'staip_netmask' :'255.255.255.0',
    'submit.htm?wan.htm': 'Send',
    'wanPPPoeConnection' :'0',
    'wan_dns1' :'10.1.1.11',
    'wanconn_type': '0',
    'wanspeed':'0',
    'wantype':'0'

}
final_url = 'http://192.168.0.1/form2Wan.cgi'
while True:
    try:
        result = session_requests.post(
            final_url,
            data = final_payload,
            headers = dict(referer = final_url)
        )
        print(result)
        print('IP Set to %s' % IP)
        break
    except Exception as e:
        print('Error Occured!!')
        print(e)
        print('Retrying\n')
        time.sleep(1)
