import pygame
from board import *

# Initialize the game and needed objects
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Chess')

# bishop = pygame.image.load('images/bishop_white.png')
# bishop = pygame.transform.scale(bishop, (100, 100))
# queen = pygame.image.load('images/queen_white.png')

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

    # Game logic
    # screen.fill((38, 41, 64))


    # screen.blit(bishop, (10, 10))
    # screen.blit(queen, (200, 200))
    
    pygame.display.update()



# pygame.draw.rect(screen, square.color, square.pos_size)
# pygame.display.update()