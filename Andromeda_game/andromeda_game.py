import sys
import pygame
import sys
from pygame.locals import *
#importar clases
from clases import jugador
#VAR
ANCHO=650
ALTO=950

#booleano juego

jugando=True


#funcion principal
def andromeda():
    pygame.init()
    ventana=pygame.display.set_mode((ANCHO,ALTO))

    #imagen fondo
    fondo=pygame.image.load("img/nebulosa.jpg")
    
    #titulo
    pygame.display.set_caption("ANDROMEDA 1.0")

    #Crer instancia de jugador
    ovni=jugador.ovni()

    #ciclo del juego
    while True:

        ventana.blit(fondo,(0,0))
        

        #Disparo del  proyectil
        if len(ovni.listaDisparo)>0:
            for x in ovni.listaDisparo:
                x.dibujar(ventana)
                x.recorrido()
                if x.rect.top<-10:
                    ovni.listaDisparo.remove(x)
        ovni.dibujar(ventana)
        ovni.mover()
        for evento in pygame.event.get():
            if evento.type==QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type==pygame.KEYDOWN:
                if evento.key==K_LEFT:
                    ovni.rect.left-=ovni.velocidad
                elif evento.key==K_RIGHT:
                    ovni.rect.right+=ovni.velocidad
                elif evento.key==K_SPACE:
                    x,y=ovni.rect.center
                    ovni.disparar(x,y)
        pygame.display.update()

#llamada a funcion principal
andromeda()