import pygame
import random
pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width , height))
pygame.display.set_caption("pet food collection")

white = (255,255,255)
green = (0 , 200 ,0)

pet = pygame.Rect(100,100,50,50)
speed = 50

food = ["carrot" , "treats"]

for i in range(5):
    x = random.randint(50,)