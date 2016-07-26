'''
Author: Philipp von Bieberstein
Date: 26.7.2016 version 1
Email: pbieberstein@gmail.com

Script to start the pygame GUI which will display the pH, EC and Temperature
value as read from the file in dashboard/data/sql_www_ap.sqlite

#####################################
       IMPORTANT INFORMATION
#####################################

1) SCRIPT HAS TO BE RUN FROM ~/dashboard/script/ directory because we use relative paths...
2) sqlite database has to be separatly updated via crontab (see README.md)


######### SOURCES #######


https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi/easy-install

https://learn.adafruit.com/raspberry-pi-pygame-ui-basics


'''

import pygame
import os
from time import sleep
import sqlite3

def draw(text, font_size, color, center_x, center_y):
    '''
    *****REQUIRES THAT SCREEN IN SETUP BEFORE CALLING THIS FUNCTION******

    Draws the specified string with the specified attributes onto the lcd screen.
    :param text: string
    :param size: int: text size // values between 0-200
    :param color: (255, 255, 255) // RGB values between 0-255
    :param center_y: y coordinate of center of text // values between 0 - 240
    :param center_x: x coordinate of center of text // values between 0 - 320
    :return: write the given text to the screen // requires screen setup before!!!
    '''
    font_size = pygame.font.Font(None, font_size)
    value = font_size.render(text, True, color)
    placement = value.get_rect(center=(center_x, center_y))
    lcd.blit(value, placement)
    return None


def get_phy_value(id):
    '''
    :param id:    "Temp -> 0"; // based on current sqlite database layout
                    "RH -> 1"; // based on current sqlite database layout
                    "pH -> 2"; // based on current sqlite database layout
                    "EC -> 3"; // based on current sqlite database layout

        // May need to be modified depending how the string comes out when read from the database (we cleared it
    from unnecessary characters
    :return: value as a string
    '''
    command = 'SELECT "value_phy" FROM sensors WHERE id == ' + str(id)
    for row in c.execute(command):
        value = row
        value = str(value).replace('(', '').replace(')', '').replace(',', '') # silly way of deleting unneeded characters
        # sorry
        return value

def get_db_time():
    '''
    Gets the timestamp from the sqlite database from when the physical values were taken.
    // May need to be modified depending how the string comes out when read from the database (we cleared it
    from unnecessary characters
    :return: time as a string
    '''
    command = 'SELECT "time" FROM sensors WHERE id == 0'
    for row in c.execute(command):
        value = row
        value = str(value).replace('(', '').replace(')', '').replace(',', '').replace("'", '').replace("u", '') # silly way of deleting unneeded characters
        # sorry
        return value


def in_range(min, max, value):
    '''
    Check if the given value is within the range between min and max.
    :param min: min value of range
    :param max:  max value of range
    :param value: value to check if it is within range
    :return: TRUE if it is in range / FALSE if outside of range
    '''
    if value > min and value < max:
        return True
    else:
        return False

def get_values():
    '''
    Returns values pH, EC, Temp as strings! // see get_phy_value(id) function
    :return: pH, EC, Temp as strings
    '''
    # Get values from database ../data/sql_www_ap.sqlite
    Temp = get_phy_value(0)
    pH = get_phy_value(2)
    EC = get_phy_value(3)

    # Round numbers for cleaner display
    pH = str(round(float(pH), 1))
    EC = str(int(round(float(EC), 0)))
    return pH, EC, Temp

###########################################
#       SETUP STANDARD VARIABLES          #
###########################################


# Setting up good ranges for pH, EC & Temp values
# Will be used later to check if current values are acceptable
ph_low, ph_high = 5, 7.2
ec_low, ec_high = 20, 1800
temp_low, temp_high = 18, 30

# Setting up standard colors for our purpose
BLACK = (0,0,0)
GRAY = (190,190,190)
GREEN = (27,169,84)
RED = (196,70,65)

##### Set Up of Display ########

os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
pygame.mouse.set_visible(False)
lcd = pygame.display.set_mode((320, 240))
lcd.fill((0,0,0))
pygame.display.update()

####### Done with setup ########



while True:
    # Set up Database connection (Should be in loop)
    try: # to make sure it doesn't fail and exit when database is updated
        conn = sqlite3.connect('../data/sql_www_ap.sqlite')
        c = conn.cursor()

        # Get value from sqlite at ../data/
        pH, EC, Temp = get_values()
        time = get_db_time()
        conn.close()

    except:
        sleep(5)
        conn = sqlite3.connect('../data/sql_www_ap.sqlite')
        c = conn.cursor()

        # Get value from sqlite at ../data/
        pH, EC, Temp = get_values()
        time = get_db_time()
        conn.close()


    lcd.fill((GRAY))

    # draw titles
    draw('pH', 20, BLACK, 50, 80)
    draw('EC', 20, BLACK, 150, 80)
    draw('C\xb0', 20, BLACK, 260, 80)
    draw(time, 20, BLACK, 160, 220)

    ################################
    ### Check if values in range ###
    ################################
    i = 0
    if in_range(ph_low, ph_high, float(pH)):
        ph_color = BLACK
    else:
        ph_color = RED
        i += 1

    if in_range(ec_low, ec_high, float(EC)):
        ec_color = BLACK
    else:
        ec_color = RED
        i += 1

    if in_range(temp_low, temp_high, float(Temp)):
        temp_color = BLACK
    else:
        temp_color = RED
        i += 1

    if i > 0:
        status = 'UNSTABLE'
        status_color = RED

    else:
        status = 'STABLE'
        status_color = GREEN

    # draw dynamic values
    draw(pH, 60, ph_color, 50, 40)
    draw(EC, 60, ec_color, 150, 40)
    draw(Temp, 60, temp_color, 260, 40)

    # draw Stable OR Unstable comment
    draw(status, 80, status_color, 160, 160)
    pygame.display.update()

    sleep(10)



