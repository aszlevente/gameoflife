import pygame
import random

pygame.init()

screen = pygame.display.set_mode((250, 250))

positions = [[1, 0, 0, 0, 0],[0, 0, 1, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 1, 0]]

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT :
            pygame.quit()

    #számolás, rajzolás
            
    d = 50
    for col in range(0, 250, d):
        for row in range(0, 250, d):
                
            dead = positions[int(row/d)][int(col/d)]
                
            if dead == 0 :
                c = (0, 0, 0)
            else :
                c = (255, 255, 255)

            pygame.draw.rect(screen, c , pygame.Rect(col, row, d, d))

    #megjelenítés
                
    pygame.display.flip()
