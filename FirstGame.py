import pygame, sys

pygame.init()
display = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Youssef H.W 3 - Solution")
while True:
    for e in pygame.event.get():
       print("hi") 
       if e.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
    pygame.display.update()