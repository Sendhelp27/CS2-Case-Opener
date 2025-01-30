import pygame
import engine as eng
import RevolverCase as RC

pygame.init()

screen = pygame.display.set_mode([1600, 500])

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.image.load

    pygame.display.flip()

pygame.quit()
