#python3

import requests

i = 0
while True:
    try:
        response = requests.get('http://10.1.131.10:8080')
        print("Request No.", i)
        print("status", response.status_code)
        i+=1
        if response.status_code == 200:
            print("\n\nIt's up man!\n\n")
            break
    except Exception as e:
        print(e)
        pass
