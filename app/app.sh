#!/usr/bin/bash

if [ "$1" = "connect" ]; then
    python app.py $1 $common_name $untrusted_ip
else
    python app.py $1 $common_name $untrusted_ip $bytes_sent $bytes_received
fi
