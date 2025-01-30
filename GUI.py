import pygame
import engine as eng
import RevolverCase as RC

pygame.init()

screen = pygame.display.set_mode([800, 450])
background = pygame.image.load("images\CSGO-Cases-background.jpg")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    pygame.display.flip()

pygame.quit()
