
'''
Python script to start the pygame GUI which will display the pH, EC and Temperature
value as read from the file in dashboard/data/values.txt
'''

'''
NEXT STEPS:
1) write script to initiate this script && load new database every 10 seconds


'''

import pygame
import os
from time import sleep
import sqlite3
#import RPi.GPIO as GPIO

def draw(text, font_size, color, center_x, center_y):
    '''
    Draws the specified string with the specified attributes onto the lcd screen.
    :param text: string
    :param size: int: 0-200
    :param color: (255, 255, 255)
    :param center_y: y coordinate of center
    :param center_x: x coordinate of center
    :return:
    '''
    font_size = pygame.font.Font(None, font_size)
    value = font_size.render(text, True, color)
    placement = value.get_rect(center=(center_x, center_y))
    lcd.blit(value, placement)
    return None


def get_phy_value(id):
    '''
    :param name:    "Temp -> 0";
                    "RH -> 1";
                    "pH -> 2";
                    "EC -> 3"
    :return:
    '''
    command = 'SELECT "value_phy" FROM sensors WHERE id == ' + str(id)
    for row in c.execute(command):
        value = row
        value = str(value).replace('(', '').replace(')', '').replace(',', '') # silly way of deleting unneeded characters
        return value

def get_db_time():
    '''
    Gets the timestamp from the sqlite database from when the physical values were taken.
    :return:
    '''
    command = 'SELECT "time" FROM sensors WHERE id == 0'
    for row in c.execute(command):
        value = row
        value = str(value).replace('(', '').replace(')', '').replace(',', '').replace("'", '').replace("u", '') # silly way of deleting unneeded characters
        return value


def in_range(min, max, value):
    if value > min and value < max:
        return True
    else:
        return False

def get_values():
    '''
    Returns values pH, EC, Temp as strings!
    :return:
    '''
    # Get values from database ../data/sql_www_ap.sqlite
    Temp = get_phy_value(0)
    pH = get_phy_value(2)
    EC = get_phy_value(3)

    # Round numbers for cleaner display
    pH = str(round(float(pH), 1))
    EC = str(int(round(float(EC), 0)))
    return pH, EC, Temp



# Setting up standard colors
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
    conn = sqlite3.connect('../data/sql_www_ap.sqlite')
    c = conn.cursor()

    # Get value from sqlite at ../data/
    pH, EC, Temp = get_values()
    time = get_db_time()

    #### FOR TESTING ###
    #pH = '7'
    #EC = '2300'
    #Temp = '21'
    ####################

    lcd.fill((GRAY))

    # draw titles
    draw('pH', 20, BLACK, 50, 80)
    draw('EC', 20, BLACK, 150, 80)
    draw('C\xb0', 20, BLACK, 260, 80)
    print(time)
    draw(time, 20, BLACK, 160, 220)

    ################################
    ### Check if values in range ###
    ################################
    i = 0
    if in_range(5,7.2,float(pH)):
        ph_color = BLACK
    else:
        ph_color = RED
        i += 1

    if in_range(1500, 3500, float(EC)):
        ec_color = BLACK
    else:
        ec_color = RED
        i += 1

    if in_range(18, 24, float(Temp)):
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
    #draw("UNSTABLE", 80, RED, 160, 160)
    #pygame.display.update()

    conn.close()

    sleep(10)



