#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 12:03:16 2023

@author: tyler
"""


import pygame
import text_analysis as gQ
import text_wrap as tw


clock = pygame.time.Clock()
running = True
display = pygame.display.set_mode((800, 600))
mousex, mousey = pygame.mouse.get_pos()
pygame.font.init()
##
font = pygame.font.Font('EraserRegular.ttf', 32)

question = "What is bothering you?"
user_ailment = ''
selected_quote = ''

box_control = False;

#Define Rctangle space for displaying font
input_space = pygame.Rect(300, 200, 800, 800)
message_space = pygame.Rect(200, 100, 800, 600)
quote_space = pygame.Rect(150, 400, 600, 600,)

#Load Objects
pygame.display.set_caption("Banzai Buddy")
bg = pygame.image.load("background.png")
derg = pygame.image.load("Derg.png")
derg_head = pygame.image.load("derg_head.png")
derg = pygame.transform.scale(derg, (300,300))
derg_head = pygame.transform.scale(derg_head,(70,70))
derg_head = pygame.transform.flip(derg_head, True, False)
derg_head2 = pygame.transform.flip(derg_head, True, False)
display.fill((255, 255, 255))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            print("Mouse click detected.")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_ailment = user_ailment[:-1]
            elif event.key == pygame.K_RETURN:
                selected_quote = gQ.getQuote(user_ailment)
                box_control = True;
                print("Enter detected")
            else:
                user_ailment += event.unicode
    
    ##Display the Dragon and the BG
    display.blit(bg, (0,0))
    display.blit(derg, (10,200))

    
    s = pygame.Surface((420,50), pygame.SRCALPHA)
    s.fill((60,60,60,128))
    display.blit(s, (200,100))
    
    #For helping to visualize the spaces.
    #pygame.draw.rect(display, (255,255,1), input_space)
    #pygame.draw.rect(display, (255,1,255), message_space)
    #pygame.draw.rect(display, (1,255,255), quote_space)
    
    ##Display Text
    
    input_surface = font.render(user_ailment, True, (1,1,1))
    tw.drawText(display, user_ailment, (1,1,1), input_space, font)
    
    display.blit(derg_head, (625,85))
    
    #display.blit(input_surface, (input_space.x+5, input_space.y+5))
    message_surface = font.render(question, True, (255,255,255))
    display.blit(message_surface, (message_space.x+5, message_space.y+5))

    if box_control == True:
        #Horrible Solution
        s = pygame.Surface((600,(len(selected_quote)/26)*47), pygame.SRCALPHA)
        s.fill((60,60,60,128))
        display.blit(s, (140,400))
        display.blit(derg_head2, (675,335))
        
    quote_surface = font.render(selected_quote, True, (255,255,255))
    #display.blit(quote_surface, (quote_space.x+5, quote_space.y+5))
    tw.drawText(display, selected_quote, (255,255,255), quote_space, font)
        
    
    
    input_space.w = min(300, input_surface.get_width()+50)
    #pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
    

pygame.quit()