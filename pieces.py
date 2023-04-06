import pygame
from variables import width, height

class Piece:
    """Define a class that describes a generic piece."""
    
    def __init__(self, color):

        self.color = color # Either 'w' or 'b'
        
        # Stores all possible moves, initially all False
        self.possible_moves = [
            [False for x_coor in range(8)] for y_coor in range(8)
        ]


    ##      PAWN        ##
class Pawn(Piece):
    """A class representing a pawn."""

    def __init__(self, color):
        super().__init__(color)

        # Import needed images
        surface_w = pygame.transform.scale(
            pygame.image.load('images/pawn_white.png'), 
            (width, height)
        )
        surface_b = pygame.transform.scale(
            pygame.image.load('images/pawn_black.png'), 
            (width, height)
        )

        # Determine image based on the color
        self.image = surface_w if color == 'w' else surface_b

    def get_possible_moves(self):
        """Gathers all possible moves and stores them."""
        self.possible_moves


        ##      KING        ##
class King(Piece):
    """A class representing a king."""

    def __init__(self, color):
        super().__init__(color)

        # Import needed images
        surface_w = pygame.transform.scale(
            pygame.image.load('images/king_white.png'), 
            (width, height)
        )
        surface_b = pygame.transform.scale(
            pygame.image.load('images/king_black.png'), 
            (width, height)
        )

        # Determine image based on the color
        self.image = surface_w if color == 'w' else surface_b


    def get_possible_moves(self):
        """Gathers all possible moves and stores them."""
        self.possible_moves = ''



        ##      KNIGHT       ##
class Knight(Piece):
    """A class representing a knight."""

    def __init__(self, color):
        super().__init__(color)

        # Import needed images
        surface_w = pygame.transform.scale(
            pygame.image.load('images/knight_white.png'), 
            (width, height)
        )
        surface_b = pygame.transform.scale(
            pygame.image.load('images/knight_black.png'), 
            (width, height)
        )

        # Determine image based on the color
        self.image = surface_w if color == 'w' else surface_b


    def get_possible_moves(self):
        """Gathers all possible moves and stores them."""
        self.possible_moves = ''



        ##      BISHOP      ##
class Bishop(Piece):
    """A class representing a bishop."""

    def __init__(self, color):
        super().__init__(color)

        # Import needed images
        surface_w = pygame.transform.scale(
            pygame.image.load('images/bishop_white.png'), 
            (width, height)
        )
        surface_b = pygame.transform.scale(
            pygame.image.load('images/bishop_black.png'), 
            (width, height)
        )

        # Determine image based on the color
        self.image = surface_w if color == 'w' else surface_b


    def get_possible_moves(self):
        """Gathers all possible moves and stores them."""
        self.possible_moves = ''



        ##      QUEEN       ##
class Queen(Piece):
    """A class representing a queen."""

    def __init__(self, color):
        super().__init__(color)

        # Import needed images
        surface_w = pygame.transform.scale(
            pygame.image.load('images/queen_white.png'), 
            (width, height)
        )
        surface_b = pygame.transform.scale(
            pygame.image.load('images/queen_black.png'), 
            (width, height)
        )

        # Determine image based on the color
        self.image = surface_w if color == 'w' else surface_b


    def get_possible_moves(self):
        """Gathers all possible moves and stores them."""
        self.possible_moves = ''



        ##      ROOK        ##
class Rook(Piece):
    """A class representing a rook."""

    def __init__(self, color):
        super().__init__(color)

        # Import needed images
        surface_w = pygame.transform.scale(
            pygame.image.load('images/rook_white.png'), 
            (width, height)
        )
        surface_b = pygame.transform.scale(
            pygame.image.load('images/rook_black.png'), 
            (width, height)
        )

        # Determine image based on the color
        self.image = surface_w if color == 'w' else surface_b


    def get_possible_moves(self):
        """Gathers all possible moves and stores them."""
        self.possible_moves = ''