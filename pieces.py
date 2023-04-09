import pygame
from variables import width, height

class Piece:
    """Define a class that describes a generic piece."""
    
    def __init__(self, color, surface_w, surface_b):

        self.color = color # Either 'w' or 'b'
        self.has_moved = False
        self.residing_square = None
        self.possible_moves = None

        # Determine image based on the color
        self.image = surface_w if color == 'w' else surface_b

        # All possible moves initialized to False
        self.clear_moves()

    
    def clear_moves(self):
        """Resets all possible moves for a piece to False."""

        self.possible_moves = [
            [False for x_coor in range(8)] for y_coor in range(8)
        ]



class Pawn(Piece):
    """A class representing a pawn."""

    def __init__(self, color):

        # Import needed images
        surface_w = pygame.transform.scale(
            pygame.image.load('images/pawn_white.png'), 
            (width, height)
        )
        surface_b = pygame.transform.scale(
            pygame.image.load('images/pawn_black.png'), 
            (width, height)
        )

        super().__init__(color, surface_w, surface_b)


    def get_possible_moves(self):
        """Gathers all possible moves for the piece and stores them."""

        self.clear_moves()
        y, x = self.residing_square.y_coor, self.residing_square.x_coor
        self.possible_moves[y - 1][x] = True

        if self.has_moved == False:
            self.possible_moves[y - 2][x] = True


class Knight(Piece):
    """A class representing a knight."""

    def __init__(self, color):

        # Import needed images
        surface_w = pygame.transform.scale(
            pygame.image.load('images/knight_white.png'), 
            (width, height)
        )
        surface_b = pygame.transform.scale(
            pygame.image.load('images/knight_black.png'), 
            (width, height)
        )

        super().__init__(color, surface_w, surface_b)


    def get_possible_moves(self):
        """Gathers all possible moves for the piece and stores them."""

        self.clear_moves()
        y, x = self.residing_square.y_coor, self.residing_square.x_coor

        # self.possible_moves[y - 2][x + 1] = True
        # self.possible_moves[y - 2][x - 1] = True
        # self.possible_moves[y + 2][x - 1] = True
        # self.possible_moves[y + 2][x - 1] = True
        # self.possible_moves[x - 2][y - 1] = True
        # self.possible_moves[x - 2][y + 1] = True
        # self.possible_moves[x + 2][y - 1] = True
        # self.possible_moves[x + 2][y + 1] = True



class Bishop(Piece):
    """A class representing a bishop."""

    def __init__(self, color):

        # Import needed images
        surface_w = pygame.transform.scale(
            pygame.image.load('images/bishop_white.png'), 
            (width, height)
        )
        surface_b = pygame.transform.scale(
            pygame.image.load('images/bishop_black.png'), 
            (width, height)
        )

        super().__init__(color, surface_w, surface_b)


    def get_possible_moves(self):
        """Gathers all possible moves for the piece and stores them."""
        self.possible_moves


class Rook(Piece):
    """A class representing a rook."""

    def __init__(self, color):

        # Import needed images
        surface_w = pygame.transform.scale(
            pygame.image.load('images/rook_white.png'), 
            (width, height)
        )
        surface_b = pygame.transform.scale(
            pygame.image.load('images/rook_black.png'), 
            (width, height)
        )

        super().__init__(color, surface_w, surface_b)


    def get_possible_moves(self):
        """Gathers all possible moves for the piece and stores them."""
        self.possible_moves


class Queen(Piece):
    """A class representing a queen."""

    def __init__(self, color):

        # Import needed images
        surface_w = pygame.transform.scale(
            pygame.image.load('images/queen_white.png'), 
            (width, height)
        )
        surface_b = pygame.transform.scale(
            pygame.image.load('images/queen_black.png'), 
            (width, height)
        )

        super().__init__(color, surface_w, surface_b)


    def get_possible_moves(self):
        """Gathers all possible moves for the piece and stores them."""
        self.possible_moves


class King(Piece):
    """A class representing a king."""

    def __init__(self, color):

        # Import needed images
        surface_w = pygame.transform.scale(
            pygame.image.load('images/king_white.png'), 
            (width, height)
        )
        surface_b = pygame.transform.scale(
            pygame.image.load('images/king_black.png'), 
            (width, height)
        )

        super().__init__(color, surface_w, surface_b)


    def get_possible_moves(self):
        """Gathers all possible moves for the piece and stores them."""
        self.possible_moves