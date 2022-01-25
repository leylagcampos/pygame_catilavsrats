import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()
ventana=pygame.display.set_mode((500,500))
pygame.display.set_caption("Movimiento usando el  mouse")
colorFondo=(1,150,70)
colorFigura=(255,255,255)
#Variables
posX,posY=randint(1,400),randint(1,300)
lado=40

while True:
    ventana.fill(colorFondo)
    pygame.draw.rect(ventana,colorFigura,(posX,posY,lado,lado))
    #detectar movimiento del mouse
    posX,posY=pygame.mouse.get_pos() #obtiene posición del  puntero del mouse
    #posicionar el puntero en el centro del cuadrado
    posX=posX-(lado/2)
    posY=posY-(lado/2)

    for evento in pygame.event.get():
        if evento.type==QUIT:
            pygame.quit()
            sys.exit()
        

    pygame.display.update()