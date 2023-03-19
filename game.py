import pygame
from board import *

# Main game loop
pygame.init()
screen = pygame.display.set_mode((500, 500))

running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             runnning = False
screen.fill((255, 0, 0))
pygame.display.update()

# square = Square(10, 10, (255, 0, 0))
# pygame.draw.rect(screen, square.color, square.pos_size)
# pygame.display.update()