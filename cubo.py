import pygame
import numpy as np
pygame.init()

# Tenho aqui vários pontos sobre uma circunferência

d = 250
cubo = np.array([[-100,-100,-100,1],[100,-100,-100,1],[-100,100,-100,1],[100,100,-100,1],[-100,-100,100,1],[100,-100,100,1],[-100,100,100,1],[100,100,100,1]]).T


M = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,-d],[0,0,-(1/d),0]])
Tz = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,350],[0,0,0,1]])
T = np.array([[1,0,0,200],[0,1,0,200],[0,0,1,0],[0,0,0,1]])


a = np.deg2rad(1)
rX = np.array([[1,0,0,0],[0,np.cos(a),-np.sin(a),0],[0,np.sin(a),np.cos(a),0],[0,0,0,1]])
ry = np.array([[np.cos(a),0,-np.sin(a),0],[0,1,0,0],[np.sin(a),0,np.cos(a),0],[0,0,0,1]])
rz = np.array([[np.cos(a),-np.sin(a),0,0],[np.sin(a),np.cos(a),0,0],[0,0,1,0],[0,0,0,1]])


R = rX @ ry @ rz

# Tamanho da tela e definição do FPS
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
FPS = 60  # Frames per Second

BLACK = (0, 0, 0)
COR_PERSONAGEM = (30, 200, 20)
COR_PONTOS = (200, 30, 20)

# Personagem
personagem = pygame.Surface((5, 5))  # Tamanho do personagem
personagem.fill(COR_PERSONAGEM)  # Cor do personagem

# Pontos 
pontos = pygame.Surface((5, 5))
pontos.fill(COR_PONTOS)  # Cor dos pontos

rodando = True
while rodando:
    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    clock.tick(FPS)
    screen.fill(BLACK)

    E = T @ M @ Tz @ R
    R = rX@ry@rz@R
    proj = E @ cubo

    # Desenhar pontos
    for i in range(proj.shape[1]):
        p = proj[:,i]
        rect = pygame.Rect([p[0]/p[3],p[1]/p[3]], (2, 2))  # First tuple is position, second is size.
        screen.blit(pontos, rect)
         
    pygame.draw.line(screen,COR_PONTOS,(proj[0,0]/proj[3,0],proj[1,0]/proj[3,0]),(proj[0,1]/proj[3,1],proj[1,1]/proj[3,1]))
    pygame.draw.line(screen,COR_PONTOS,(proj[0,1]/proj[3,1],proj[1,1]/proj[3,1]),(proj[0,3]/proj[3,3],proj[1,3]/proj[3,3]))
    pygame.draw.line(screen,COR_PONTOS,(proj[0,3]/proj[3,3],proj[1,3]/proj[3,3]),(proj[0,2]/proj[3,2],proj[1,2]/proj[3,2]))
    pygame.draw.line(screen,COR_PONTOS,(proj[0,0]/proj[3,0],proj[1,0]/proj[3,0]),(proj[0,2]/proj[3,2],proj[1,2]/proj[3,2]))

    pygame.draw.line(screen,COR_PONTOS,(proj[0,4]/proj[3,4],proj[1,4]/proj[3,4]),(proj[0,5]/proj[3,5],proj[1,5]/proj[3,5]))
    pygame.draw.line(screen,COR_PONTOS,(proj[0,5]/proj[3,5],proj[1,5]/proj[3,5]),(proj[0,7]/proj[3,7],proj[1,7]/proj[3,7]))
    pygame.draw.line(screen,COR_PONTOS,(proj[0,7]/proj[3,7],proj[1,7]/proj[3,7]),(proj[0,6]/proj[3,6],proj[1,6]/proj[3,6]))
    pygame.draw.line(screen,COR_PONTOS,(proj[0,6]/proj[3,6],proj[1,6]/proj[3,6]),(proj[0,4]/proj[3,4],proj[1,4]/proj[3,4]))

    pygame.draw.line(screen,COR_PONTOS,(proj[0,0]/proj[3,0],proj[1,0]/proj[3,0]),(proj[0,4]/proj[3,4],proj[1,4]/proj[3,4]))
    pygame.draw.line(screen,COR_PONTOS,(proj[0,1]/proj[3,1],proj[1,1]/proj[3,1]),(proj[0,5]/proj[3,5],proj[1,5]/proj[3,5]))
    pygame.draw.line(screen,COR_PONTOS,(proj[0,2]/proj[3,2],proj[1,2]/proj[3,2]),(proj[0,6]/proj[3,6],proj[1,6]/proj[3,6]))
    pygame.draw.line(screen,COR_PONTOS,(proj[0,3]/proj[3,3],proj[1,3]/proj[3,3]),(proj[0,7]/proj[3,7],proj[1,7]/proj[3,7]))

    pygame.display.flip()
    # Update!
    pygame.display.update()

# Terminar tela
pygame.quit()