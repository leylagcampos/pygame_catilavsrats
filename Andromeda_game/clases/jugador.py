import pygame
from clases import disparo

class ovni(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenOvni=pygame.image.load("img/ovni.png")
        self.imagenExplo=pygame.image.load("img/explo.png")
        #Tomamos rectangulo imagen
        self.rect=self.imagenOvni.get_rect()

        #Posicion de la nave
        self.rect.centerx=240
        self.rect.centery=900
        self.velocidad=20
        self.vida=True
        self.listaDisparo=[]
        self.sonidoDisparo=pygame.mixer.Sound("sonidos/disparo.mp3")

    def mover(self):
        if self.vida==True:
            if self.rect.left<=0:
                self.rect.left=0
            elif self.rect.right>650:
                self.rect.right=650
    
    def disparar(self,x,y):
        if self.vida==True:
            #print("disparando")
            misil=disparo.misil(x,y)
            self.listaDisparo.append(misil)
            self.sonidoDisparo.play()

    def dibujar(self, superficie):
        if self.vida==True:
            superficie.blit(self.imagenOvni,self.rect)
        else:
            superficie.blit(self.imagenExplo,self.rect)
