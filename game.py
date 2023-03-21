import pygame
from board import *

# Initialize the game
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Chess')

# Build the board
board = Board(screen)
board.initial_setup()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            coor = pygame.mouse.get_pos()
            # Handle any click event
            board.click(coor[0], coor[1])
            

    # Update the screen
    pygame.display.update()

# Once loops has been broken
pygame.quit()

# for row in board.squares:
#     for square in row:
#         if square.is_selected:
#             print(square.occupying_piece.x_coor, square.occupying_piece.y_coor)
