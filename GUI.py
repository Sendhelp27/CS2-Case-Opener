import pygame
import engine as eng
import RevolverCase as RC

pygame.init()

screen = pygame.display.set_mode([1600, 900])
background = pygame.image.load("images/CSGO-Cases-background.jpg")

original_size = background.get_size()

# Double the size of the image
new_size = (original_size[0] * 2, original_size[1] * 2)
background = pygame.transform.scale(background, new_size)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    pygame.display.flip()

pygame.quit()
