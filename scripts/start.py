
'''
Python script to start the pygame GUI which will display the pH, EC and Temperature
value as read from the file in dashboard/data/values.txt
'''

'''
NEXT STEPS:
1) Read values from file
2) Program acceptable Range of pH & EC values
3) Depending on that display 'stable' or 'unstable'
4) Color 'RED' whatever specific value is unacceptable
'''

import pygame
import os
from time import sleep
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


BLACK = (0,0,0)
GRAY = (190,190,190)
GREEN = (27,169,84)
RED = (196,70,65)


# Set Up of Display
os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
pygame.mouse.set_visible(False)
lcd = pygame.display.set_mode((320, 240))
lcd.fill((0,0,0))
pygame.display.update()

i = 1

while True:
    lcd.fill((GRAY))
    i += 1
    # draw titles
    draw('pH', 20, BLACK, 50, 80)
    draw('EC', 20, BLACK, 150, 80)
    draw('C\xb0', 20, BLACK, 260, 80)


    # draw dynamic values
    draw('5.2', 60, BLACK, 50, 40)
    draw('2300', 60, BLACK, 150, 40)
    draw('19.7', 60, BLACK, 260, 40)


    # draw Stable OR Unstable comment
    if i%2 == 1:
        draw('STABLE', 80, GREEN, 160, 160)
        pygame.display.update()
    else:
        draw("UNSTABLE", 80, RED, 160, 160)
        pygame.display.update()

    sleep(0.4)

'''
    sleep(3)
    lcd.fill(GRAY)
    lcd.blit(font_small.render('pH', True, BLACK), rect)
    pygame.display.update()
    sleep(3)
    lcd.fill(GRAY)
    lcd.blit(font_big.render('EC', True, BLACK), rect)
    pygame.display.update()
'''




