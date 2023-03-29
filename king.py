import pygame
from piece import Piece
from variables import *

# Import needed objects
surface_w = pygame.transform.scale(
    pygame.image.load('images/king_white.png'), 
    (width, height)
)
surface_b = pygame.transform.scale(
    pygame.image.load('images/king_black.png'), 
    (width, height)
)

class King(Piece):
    """A class representing a king."""

    def __init__(self, color):
        super().__init__(color)

        # Determine image based on the color
        self.image = surface_w if color == 'w' else surface_b