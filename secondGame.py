import pygame, sys

pygame.init()

# Colors: 
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# DEFALUT Background:
backgroundColor = WHITE

# Dictionary: 
key_dic = { pygame.K_r: RED, pygame.K_g: GREEN, pygame.K_b: BLUE, pygame.K_w: WHITE, pygame.K_k: BLACK }


# Defined Screen:
screen = pygame.display.set_mode((600, 500))

# Caption: 
pygame.display.set_caption("Colors in Python")

while True:
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key in key_dic:
                backgroundColor = key_dic[e.key]

        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        screen.fill(backgroundColor)

    pygame.display.flip()