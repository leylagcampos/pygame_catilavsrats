import sys
import pygame
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

puntos=0
colorFuente=(255,255,255)
#booleano juego

jugando=True

#Cargar asteroides
def cargarAsteroide(x,y):
    astro=asteroide.astro(x,y)
    listaAsteroide.append(astro)

def gameOver():
    global jugando
    jugando=False
    for astros in listaAsteroide:
        listaAsteroide.remove(astros)

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

    #Sonidos
    pygame.mixer.music.load("sonidos/andromedavoices.mp3")
    pygame.mixer.music.play(5)
    sonidocolision=pygame.mixer.Sound("sonidos/colision.mp3")

    #Marcadorfuente
    fuenteMarcador=pygame.font.SysFont("Consolas",30)


    #ciclo del juego
    while True:

        ventana.blit(fondo,(0,0))
        
        # Tiempo
        tiempo=perf_counter()
        #Marcador
        global puntos
        textoMarcador=fuenteMarcador.render("Puntos:" + str(puntos),0,colorFuente)
        ventana.blit(textoMarcador,(0,0))
        #creamos asteroides
        if tiempo-contador>1:
            contador=tiempo
            posX=randint(200,450)
            cargarAsteroide(posX,0)

        #comprobar lista asteroide
        if len(listaAsteroide)>0:
            for x in listaAsteroide:
                if jugando==True:
                    x.dibujar(ventana)
                    x.recorrido()
                if x.rect.top>950:
                    listaAsteroide.remove(x)
                else:
                    if x.rect.colliderect(ovni.rect):
                        listaAsteroide.remove(x)
                        sonidocolision.play()
                        #print("Colision ovni/astro")
                        ovni.vida=False
                        gameOver()


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
                            puntos+=1
                            #print("Colision disparo/astro")

        ovni.dibujar(ventana)
        ovni.mover()
        for evento in pygame.event.get():
            if evento.type==QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type==pygame.KEYDOWN:
                if jugando==True:
                    if evento.key==K_LEFT:
                        ovni.rect.left-=ovni.velocidad
                    elif evento.key==K_RIGHT:
                        ovni.rect.right+=ovni.velocidad
                    elif evento.key==K_SPACE:
                        x,y=ovni.rect.center
                        ovni.disparar(x,y)
        if jugando==False:
            FuenteGameOver=pygame.font.SysFont("Consolar",60)
            textoGameOver=FuenteGameOver.render("Game Over",0,colorFuente)
            ventana.blit(textoGameOver,(220,450))
            pygame.mixer.music.fadeout(3000)

        pygame.display.update()

#llamada a funcion principal
andromeda()