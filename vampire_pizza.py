import pygame
from pygame import *
pygame.init()

WINDOW_WIDTH = 1100
WINDOW_HEIGHT=600
WINDOW_RES=(WINDOW_WIDTH, WINDOW_HEIGHT)

WIDTH=100
HEIGHT=100
WHITE=(255,255,255)
tile_color=WHITE

GAME_WINDOW = display.set_mode(WINDOW_RES)
display.set_caption('Attack of the Vampire Zombies')

background_img=image.load(r'.\gameassets\restaurant.jpg')
background_surf=Surface.convert_alpha(background_img)
BACKGROUND=transform.scale(background_surf, WINDOW_RES)



pizza_img=image.load(r'.\gameassets\vampire.png')
#loads image into program
pizza_surf=Surface.convert_alpha(pizza_img)
#Convert image to a surface (images in python), changes format so that our game window can use it
VAMPIRE_PIZZA = transform.scale(pizza_surf, (WIDTH, HEIGHT))
#Adjusts size of image

for row in range(6):
    draw.rect(BACKGROUND, tile_color, (0,HEIGHT*row, WIDTH, HEIGHT), 1)
    for column in range(11):
        draw.rect(BACKGROUND, tile_color, (WIDTH*column, HEIGHT*row, WIDTH, HEIGHT),1)

GAME_WINDOW.blit(BACKGROUND, (0,0))
GAME_WINDOW.blit(VAMPIRE_PIZZA, (900,400))
# blit is display,display vampire pizza at 900 by 400 pixels,GAME_WINDOW.blit(surface,(location tuple))



game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_running = False
    display.update()
pygame.quit()
