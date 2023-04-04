import pygame
import pygame.mixer

import numpy as np

pygame.init()
musica = pygame.mixer.Sound("amor.mp3")
musica.play()

# Tenho aqui vários pontos sobre uma circunferência

d = 200
cubo = np.array([[-100,-100,-100,1],[100,-100,-100,1],[-100,100,-100,1],[100,100,-100,1],[-100,-100,100,1],[100,-100,100,1],[-100,100,100,1],[100,100,100,1]]).T


M = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,-d],[0,0,-(1/d),0]])
Tz = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,350],[0,0,0,1]])
T = np.array([[1,0,0,200],[0,1,0,200],[0,0,1,0],[0,0,0,1]])


a = np.deg2rad(1)
rx = np.array([[1,0,0,0],[0,np.cos(a),-np.sin(a),0],[0,np.sin(a),np.cos(a),0],[0,0,0,1]])
ry = np.array([[np.cos(a),0,-np.sin(a),0],[0,1,0,0],[np.sin(a),0,np.cos(a),0],[0,0,0,1]])
rz = np.array([[np.cos(a),-np.sin(a),0,0],[np.sin(a),np.cos(a),0,0],[0,0,1,0],[0,0,0,1]])


# Tamanho da tela e definição do FPS
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
FPS = 60  # Frames per Second

BLACK = (0, 0, 0)
COR_ARESTAS = (224, 61, 20)
laranja = (224, 61, 20)
azul = (24, 8, 199)

# Personagem
personagem = pygame.Surface((5, 5))  # Tamanho do personagem
personagem.fill(COR_ARESTAS)  # Cor do personagem

r = rx@ry@rz
ident = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
R =ident
a = np.deg2rad(1)

direcao = [np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]),np.linalg.inv(ry),ry,rx,np.linalg.inv(rx),rz,np.linalg.inv(rz)]
d = 0
rodando = True
free = True
while rodando:
    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                rodando = False
            elif event.key == pygame.K_r:
                R = ident
                d = 0
            elif event.key == pygame.K_d:
                d = 1
            elif event.key == pygame.K_a:
                d = 2
            elif event.key == pygame.K_w:
                d = 3
            elif event.key == pygame.K_s:
                d = 4
            elif event.key == pygame.K_l:
                d = 5
            elif event.key == pygame.K_k:
                d = 6
            elif event.key == pygame.K_f:
                free = not free
                if COR_ARESTAS==laranja:
                    COR_ARESTAS=azul
                else:
                    COR_ARESTAS=laranja
        elif event.type == pygame.KEYUP and not free:
            d=0
    R = direcao[d]@R
    clock.tick(FPS)
    screen.fill(BLACK)

    E = T @ M @ Tz @ R
    proj = E @ cubo

    w = 5
    pygame.draw.line(screen,COR_ARESTAS,(proj[0,0]/proj[3,0],proj[1,0]/proj[3,0]),(proj[0,1]/proj[3,1],proj[1,1]/proj[3,1]),width=w)
    pygame.draw.line(screen,COR_ARESTAS,(proj[0,1]/proj[3,1],proj[1,1]/proj[3,1]),(proj[0,3]/proj[3,3],proj[1,3]/proj[3,3]),width=w)
    pygame.draw.line(screen,COR_ARESTAS,(proj[0,3]/proj[3,3],proj[1,3]/proj[3,3]),(proj[0,2]/proj[3,2],proj[1,2]/proj[3,2]),width=w)
    pygame.draw.line(screen,COR_ARESTAS,(proj[0,0]/proj[3,0],proj[1,0]/proj[3,0]),(proj[0,2]/proj[3,2],proj[1,2]/proj[3,2]),width=w)

    pygame.draw.line(screen,COR_ARESTAS,(proj[0,4]/proj[3,4],proj[1,4]/proj[3,4]),(proj[0,5]/proj[3,5],proj[1,5]/proj[3,5]),width=w)
    pygame.draw.line(screen,COR_ARESTAS,(proj[0,5]/proj[3,5],proj[1,5]/proj[3,5]),(proj[0,7]/proj[3,7],proj[1,7]/proj[3,7]),width=w)
    pygame.draw.line(screen,COR_ARESTAS,(proj[0,7]/proj[3,7],proj[1,7]/proj[3,7]),(proj[0,6]/proj[3,6],proj[1,6]/proj[3,6]),width=w)
    pygame.draw.line(screen,COR_ARESTAS,(proj[0,6]/proj[3,6],proj[1,6]/proj[3,6]),(proj[0,4]/proj[3,4],proj[1,4]/proj[3,4]),width=w)

    pygame.draw.line(screen,COR_ARESTAS,(proj[0,0]/proj[3,0],proj[1,0]/proj[3,0]),(proj[0,4]/proj[3,4],proj[1,4]/proj[3,4]),width=w)
    pygame.draw.line(screen,COR_ARESTAS,(proj[0,1]/proj[3,1],proj[1,1]/proj[3,1]),(proj[0,5]/proj[3,5],proj[1,5]/proj[3,5]),width=w)
    pygame.draw.line(screen,COR_ARESTAS,(proj[0,2]/proj[3,2],proj[1,2]/proj[3,2]),(proj[0,6]/proj[3,6],proj[1,6]/proj[3,6]),width=w)
    pygame.draw.line(screen,COR_ARESTAS,(proj[0,3]/proj[3,3],proj[1,3]/proj[3,3]),(proj[0,7]/proj[3,7],proj[1,7]/proj[3,7]),width=w)

    pygame.display.flip()
    # Update!
    pygame.display.update()

# Terminar tela
pygame.quit()