#!/bin/sh
key=$1
val=$2
if [ "$val" = "reload" ]; then
	app=$key
	key=/applications/$app/environment
	val="{\"gen\":\"$(date +%s)\"}"
fi
sudo curl -X PUT -d $val --unix-socket /var/run/control.unit.sock http://localhost/config$key
