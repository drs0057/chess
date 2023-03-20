import pygame
from piece import Piece

# Import needed objects
surface = pygame.image.load('images/bishop_white.png')
surface = pygame.transform.scale(surface, (100, 100))

class Bishop(Piece):
    """A class representing a bishop."""

    def __init__(self):
        super().__init__()
        self.image = surface