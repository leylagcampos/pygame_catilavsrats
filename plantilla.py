import pygame
import sys
from pygame.locals import *

pygame.init()
ventana=pygame.display.set_mode((500,500))
pygame.display.set_caption("Catila vs Rats")
colorFondo=(1,150,70)


while True:
    ventana.fill(colorFondo)
    for evento in pygame.event.get():
        if evento.type==QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()