## Automate IIT (BHU) LAN Authentication 

This code automates the authentication process of IIT (BHU) LAN.

## Dependencies:

* Python 3

### Instructions:

To authenticate your system on LAN, set your username and password in `lan_auth.py` and run:

	python lan_auth.py

If you wanna forget about LAN Authentication forever, run:

	nohup ./run.sh &

This will check for LAN Authentication every 10 seconds in the background. Add the above command as startup application to run this script in the background after every system boot.

Enjoy!



