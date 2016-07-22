#!/bin/bash

# No password needed because I set up ssh key pair in the host server and Raspi


sudo python monitor.py &&
echo <<<started python script>>>

while [ 1 ]
do
    echo Downloading Database
    scp -P13332 paja@160.217.215.233:/home/paja/WWW/sql_www_ap.sqlite ../data/
    echo Download complete
    echo sleeping for 1 minute... thank you
    sleep 60
done