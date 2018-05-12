#!/bin/sh

# this script will run  `lan_auth.py` every 10 seconds
while true
do
	my_dir=`dirname $0`
	python $my_dir/lan_auth.py
    sleep 10
done
