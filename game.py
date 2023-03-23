import pygame
from board import *
from variables import *

# Initialize the game
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(background_color)
pygame.display.set_caption('Chess')
clock = pygame.time.Clock()

# Build the board
board = Board(screen)
board.initial_setup()

# Main game loop
running = True
while running:

    # Limit the framerate
    clock.tick(60)

    for event in pygame.event.get():

        # If window is closed
        if event.type == pygame.QUIT:
            running = False

        # If a square is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            coor = pygame.mouse.get_pos()
            # Handle any click event
            board.click(coor[0], coor[1])

    # If a player runs out of time
    if board.current_player.time_remaining_ms <= 0:
        running = False
        pygame.quit()

    # Count down the clock
    board.timer(board.current_player, screen)

    # Update the screen
    pygame.display.update()

# Once loop has been broken
pygame.quit()