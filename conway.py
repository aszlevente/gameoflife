import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))

#Glider
positions = [(11, 9), (12, 9), (13, 9), (13, 8), (12, 7)]

# Toad
#positions = [(11, 9), (12, 9), (13, 9), (10, 10), (11, 10), (12, 10)]

while True:
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT :
            pygame.quit()

    #számolás, rajzolás

    phantomPositions = positions.copy()
    
    d = 20
    
    for col in range(0, 800, d):
        for row in range(0, 600, d):
            
            if ((col/d),(row/d)) in phantomPositions :
                counter = -1
            else :
                counter = 0
                
            for i in range(-1, 2) :
                for l in range(-1, 2) :
                    for pos in phantomPositions :
                        if int(col/d)+i == pos[0] and int(row/d)+l == pos[1] :
                            counter += 1
                            break
            
            if (col/d, row/d) not in phantomPositions and counter == 3 :
                #resurrection
                c = (255, 255, 255)
                positions.append((col/d, row/d))
            elif (col/d, row/d) in phantomPositions and counter in (2, 3) :
                #keeps living
                c = (255, 255, 255)
            else :
                c = (0, 0, 0)
                if (col/d, row/d) in phantomPositions :
                    positions.pop(positions.index((col/d, row/d)))

            pygame.draw.rect(screen, c , pygame.Rect(col, row, d, d))

    #megjelenítés
                
    pygame.display.flip()
    time.sleep(1)
    

