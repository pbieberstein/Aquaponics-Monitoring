#!/bin/bash

# No password needed because I set up ssh key pair in the host server and Raspi


sudo python start.py

while [ 1 ]
do
    scp -P13332 paja@160.217.215.233:/home/paja/WWW/sql_www_ap.sqlite ../data/
    sleep 10
done