
'''
Python script to start the pygame GUI which will display the pH, EC and Temperature
value as read from the file in dashboard/data/values.txt
'''

import pygame
import os
from time import sleep
import RPi.GPIO as GPIO



BLACK = (0,0,0)
GRAY = (190,190,190)
BLUE = (0,0,255)
RED = (255,0,0)

os.putenv('SDL_FBDEV', '/dev/fb1')

pygame.init()
pygame.mouse.set_visible(False)
lcd = pygame.display.set_mode((320, 240))
lcd.fill((0,0,0))
pygame.display.update()

font_big = pygame.font.Font(None, 60)
font_small = pygame.font.Font(None, 20)

while True:
        lcd.fill((GRAY))
        # Draw pH value and title
        ph_value = font_big.render('5.8', True, BLACK)
        placement = ph_value.get_rect(center=(50,40))
        lcd.blit(ph_value, placement)

        ph_title = font_small.render('pH', True, BLACK)
        placement = ph_title.get_rect(center=(50,80))

        lcd.blit(ph_title, placement)

        # Draw EC value and title
        ec_value = font_big.render('2300', True, BLACK)
        placement = ec_value.get_rect(center=(150,40))
        lcd.blit(ec_value, placement)

        ec_title = font_small.render('EC', True, BLACK)
        placement = ec_title.get_rect(center=(150,80))

        lcd.blit(ec_title, placement)


        # Draw Temp value and title
        ec_value = font_big.render('23.2', True, BLACK)
        placement = ec_value.get_rect(center=(260,40))
        lcd.blit(ec_value, placement)

        ec_title = font_small.render('C\xb0', True, BLACK)
        placement = ec_title.get_rect(center=(260,80))

        lcd.blit(ec_title, placement)

        pygame.display.update()


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




