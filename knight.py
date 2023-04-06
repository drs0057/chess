import pygame
from piece import Piece
from variables import width, height

# Import needed objects
surface_w = pygame.transform.scale(
    pygame.image.load('images/knight_white.png'), 
    (width, height)
)
surface_b = pygame.transform.scale(
    pygame.image.load('images/knight_black.png'), 
    (width, height)
)

class Knight(Piece):
    """A class representing a knight."""

    def __init__(self, color):
        super().__init__(color)

        # Determine image based on the color
        self.image = surface_w if color == 'w' else surface_b


    def get_possible_moves(self):
        """Gathers all possible moves and stores them."""

        self.possible_moves = ''