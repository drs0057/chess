import pygame
from piece import Piece

# Import needed objects
surface_w = pygame.transform.scale(
    pygame.image.load('images/king_white.png'), 
    (100, 100)
)
surface_b = pygame.transform.scale(
    pygame.image.load('images/king_black.png'), 
    (100, 100)
)

class King(Piece):
    """A class representing a king."""

    def __init__(self, x_coor, y_coor, color):
        super().__init__(x_coor, y_coor, color)

        # Determine image based on the color
        self.image = surface_w if color == 'w' else surface_b