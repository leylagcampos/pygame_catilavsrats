import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()
ventana=pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Imagen y posicion al azar con randint")
colorFondo=(1,150,70)
colorRectangulo=(255,60,40)
#carga de imagen
imagen=pygame.image.load("imagenes/feliz-cumple.jpg")
#posision de la imagen
posX,posY=(0,0)
while True:
    ventana.fill(colorFondo)
    ventana.blit(imagen,(posX,posY))
    for i in range(20):
        posX2,posY2=randint(1,1000), randint(1,1000)
        r,g,b=randint(0,255),randint(0,255),randint(0,255)
        colorRectangulo=(r,g,b)
        pygame.draw.rect(ventana,colorRectangulo,(posX2,posY2,40,40))

    for evento in pygame.event.get():
        if evento.type==QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()