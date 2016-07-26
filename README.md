# Hydrook (Hydroponics Monitoring)
# 
#
## ABOUT
*Hydrook* is a lightweight script that uses a Raspberry Pi with 2.8" TFT Resistive touch screen to display real-time values of pH, EC & Temperature values of a hydroponic or aquaponic system via a sqlite database.
#
![Stable Photo](https://github.com/pbieberstein/dashboard/blob/master/samples/stable_sample.jpg?raw=true)
![Unstable Photo](https://github.com/pbieberstein/dashboard/blob/master/samples/unstable_sample.jpg?raw=true)


## Prerequisites 
*(This is what we used - it may work with other specs too)*
- Raspberry Pi B+
- 2.8" TFT resistive Touchscreen
- Raspbian Jessie (https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi/easy-install)
- Sqlite database with the values that you want to display 

>Its easiest if its in the same format as in /dashboard/data/sql_www_ap.sqlite >(use http://inloop.github.io/sqlite-viewer/ to display format)

## Quickstart
- Follow the Adafruit tutorial to set up your screen https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi/easy-install
- Clone this repo
```sh
git clone https://github.com/pbieberstein/dashboard.git
```
- Set up Cron job to continually update database (see our way below)
- Set up Cron job to start script at reboot (see our way below) 

## Modify
>You can modify which pH, EC and Temperature values are acceptable inside the /scripts/monitor.py script. In the 'setup variables' section, simply insert the range of values you see as Stable or Unstable.


## Our Crontab Jobs
```sh
sudo crontab -e
```
add the line (our script needs to be run as root)
>@reboot cd /home/pi/dashboard/scripts && python monitor.py &

```sh
crontab -e
```
add the line (update of database doesn't have to be root)
>*/1 * * * * cd /home/pi/dashboard/scripts && scp username@remote.ip.address:/path/to/database

# Author
Philipp v. Bieberstein (pbieberstein@gmail.com)
- Built during Summer School project at Institute of Complex Systems in Nové Hrady, Czech Republic


# References
- https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi/easy-install

- https://learn.adafruit.com/raspberry-pi-pygame-ui-basics
