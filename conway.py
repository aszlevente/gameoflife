import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

positions = [(0, 20), (11, 10), (11, 13)]

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT :
            pygame.quit()

    #számolás, rajzolás
            
    d = 20
    for col in range(0, 800, d):
        for row in range(0, 600, d):

            for i in range(-1, 2) :
                for l in range(-1, 2) :
                    for pos in positions :
                        if int(col/d) == pos[0] and int(row/d) == pos[1] :
                            counter += 1
                        break
            
            
            c = (0, 0, 0)
            for pos in positions :
                if int(col/d) == pos[0] and int(row/d) == pos[1] :
                    c = (255, 255, 255)
                    break

            pygame.draw.rect(screen, c , pygame.Rect(col, row, d, d))

    #megjelenítés
                
    pygame.display.flip()

