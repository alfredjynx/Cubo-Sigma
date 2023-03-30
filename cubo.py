import pygame
import numpy as np
pygame.init()

# Tenho aqui vários pontos sobre uma circunferência

d = 200
cubo = np.array([[100,100,1,1],[300,100,1,1],[100,300,1,1],[300,300,1,1],[100,100,200,1],[300,100,200,1],[100,300,200,1],[300,300,200,1]]).T

M = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,-d],[0,0,-(1/d),0]])

# Controle de tempo
t = 0

# Velocidade angular (rotacoes por segundo)
v = 0.2

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

    # Controlar frame rate
    clock.tick(FPS)

    # Movimento do personagem

    # Desenhar fundo
    screen.fill(BLACK)

    proj = M @ cubo

    T = np.array([[1,0,0,200],[0,1,0,200],[0,0,1,0],[0,0,0,1]])

    proj_t = T @ proj

    # Desenhar pontos
    for p in range(proj_t.shape[1]):
        point = proj_t[:,p]
        
        rect = pygame.Rect([point[0]/point[3],point[1]/point[3]], (2, 2))  # First tuple is position, second is size.
        screen.blit(pontos, rect)
    

    # Update!
    pygame.display.update()

# Terminar tela
pygame.quit()