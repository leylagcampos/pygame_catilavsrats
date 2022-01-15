import pygame
import sys
from pygame.locals import *

pygame.init()
ventana=pygame.display.set_mode((500,500))
pygame.display.set_caption("Catila vs Rats")
colorFondo=(1,150,70)
colorLinea=(0,0,255)
colorCirculo=(255,255,0)
colorFigura=(0,255,0)
colorPoligono=(200,200,100)

while True:
    ventana.fill(colorFondo)
    ##Lineas
    pygame.draw.line(ventana,colorLinea,(20,30),(140,120),10)   #coordenadas inicio,coordfin,ancho 
    ##Figuras
    pygame.draw.rect(ventana,colorFigura,(100,100,300,150))   #coord,ancho y alto
    pygame.draw.polygon(ventana,colorPoligono,((300,250),(400,160),(330,300),(200,300),(100,200)))
    ##Circulo
    pygame.draw.circle(ventana,colorCirculo,(100,140),100,30)  #coordenadas,radio,ancho
 
    for evento in pygame.event.get():
        if evento.type==QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()