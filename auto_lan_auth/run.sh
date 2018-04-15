#!/bin/sh

# this script will run  `lan_auth.py` every 10 seconds
while true
do 
    python lan_auth.py
    sleep 10
done
