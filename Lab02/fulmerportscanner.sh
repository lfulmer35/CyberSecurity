#!/bin/bash
echo "Lucas Fulmer, Bash Portscanner" #where is your name


if [ $1="-h" ] || [ $1="--help" ]; then
	echo "USAGE: $0 192.168.10.3 1 100 will can ports 1-100";
fi
host=$1
startport=$2
stopport=$3

#ping a device to see if it is up
#this will check to see if the ip addresses are in use
function pingcheck
{
	echo "checking ip addresses..."
	numPing=`ping -c 1 $host | grep bytes | wc -l`

	if [ "$numPing" -gt 1 ]; then
		echo "$host is up"
	else
		echo "$host is down...quitting"
		exit
	fi
}

#test a port to see if it's open
#this function is using a for loop to check all ports from start to stop
function portcheck
{
	echo "checking ports..."
	for(( port=$startport; port<=$stopport; port++ ))
	do
		(echo > /dev/tcp/$host/$port) > /dev/null 2>&1 &&
		echo "$port open"
			done
}

pingcheck
portcheck
echo "Complete"
