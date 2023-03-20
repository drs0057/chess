import pygame
from board import *

# Initialize the game
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Chess')

# Initialize needed objects


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    # Build the board
    board = Board()
    squares = board.build_square_objects(screen)
    board.print_squares(squares)

    # Place pieces

    # Game logic

    pygame.display.update()