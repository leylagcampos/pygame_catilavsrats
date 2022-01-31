import sys
import pygame
import sys
from pygame.locals import *
#importar clases
from clases import jugador
from clases import asteroide
from random import randint
from time import perf_counter

#VAR
ANCHO=650
ALTO=950

listaAsteroide=[]
#booleano juego

jugando=True

#Cargar asteroides
def cargarAsteroide(x,y):
    astro=asteroide.astro(x,y)
    listaAsteroide.append(astro)

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

    contador=0
    #ciclo del juego
    while True:

        ventana.blit(fondo,(0,0))
        
        # Tiempo
        tiempo=perf_counter()
        #creamos asteroides
        if tiempo-contador>1:
            contador=tiempo
            posX=randint(200,450)
            cargarAsteroide(posX,0)

        #comprobar lista asteroide
        if len(listaAsteroide)>0:
            for x in listaAsteroide:
                x.dibujar(ventana)
                x.recorrido()
                if x.rect.top>950:
                    listaAsteroide.remove(x)
                else:
                    if x.rect.colliderect(ovni.rect):
                        listaAsteroide.remove(x)
                        print("Colision ovni/astro")
                        #gameover()


        #Disparo del  proyectil
        if len(ovni.listaDisparo)>0:
            for x in ovni.listaDisparo:
                x.dibujar(ventana)
                x.recorrido()
                if x.rect.top<-10:
                    ovni.listaDisparo.remove(x)
                else:
                    for astros in listaAsteroide:
                        if x.rect.colliderect(astros.rect):
                            listaAsteroide.remove(astros)
                            ovni.listaDisparo.remove(x)
                            print("Colision disparo/astro")

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