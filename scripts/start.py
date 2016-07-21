

'''
Python script to start the pygame GUI which will display the pH, EC and Temperature
value as read from the file in dashboard/data/values.txt
'''

import pygame
import os
from time import sleep


WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
pygame.init()
pygame.mouse.set_visible(False)
lcd = pygame.display.set_mode((320, 240))
lcd.fill((0,0,0))
pygame.display.update()

font_big = pygame.font.Font(None, 60)

while True:
        lcd.fill((122,133,2))
        text_surface = font_big.render('Hi', True, WHITE)
        rect = text_surface.get_rect(center=(160,120))
        lcd.blit(text_surface, rect)
        pygame.display.update()
        sleep(3)
        lcd.fill((0,0,255))
        lcd.blit(font_big.render('pH', True, RED), rect)
        pygame.display.update()
        sleep(3)
        lcd.fill((0,255,0))
        lcd.blit(font_big.render('SIIIIIWYYEEEEE', True, BLUE), rect)
        pygame.display.update()
        sleep(3)




