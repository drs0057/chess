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


    def add_moves(self):
        """Adds moves to piece's possilbe moves."""
        for dy, dx in self.moves:
            new_y = self.residing_square.y_coor + dy
            new_x = self.residing_square.x_coor + dx
            if new_y in range(8) and new_x in range(8):
                self.possible_moves[new_y][new_x] = True


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
        self.moves = [(-1, 0), (-2, 0)]
        super().__init__(color, surface_w, surface_b)


    def get_possible_moves(self):
        """Gathers all possible moves for the piece and stores them."""
        self.clear_moves()

        # If the pawn has moved, remove the initial double move
        if self.has_moved == True:
            try:
                self.moves.pop(1)
            except IndexError:
                pass
        self.add_moves()


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
        self.moves = [
            (-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2)
        ]
        super().__init__(color, surface_w, surface_b)


    def get_possible_moves(self):
        """Gathers all possible moves for the piece and stores them."""
        self.clear_moves()
        self.add_moves()


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
        self.moves = (
            [(i, i) for i in range(1, 8)] +
            [(-i, -i) for i in range(1, 8)] +
            [(-i, i) for i in range(1, 8)] +
            [(i, -i) for i in range(1, 8)]
        )


    def get_possible_moves(self):
        """Gathers all possible moves for the piece and stores them."""
        self.clear_moves()
        self.add_moves()


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
        self.moves = (
            [(i, 0) for i in range(1, 8)] + 
            [(-i, 0) for i in range(1, 8)] + 
            [(0, i) for i in range(1, 8)] + 
            [(0, -i) for i in range(1, 8)]
        )


    def get_possible_moves(self):
        """Gathers all possible moves for the piece and stores them."""
        self.clear_moves()
        self.add_moves()


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
        self.moves = (
            [(i, i) for i in range(1, 8)] +
            [(-i, -i) for i in range(1, 8)] +
            [(-i, i) for i in range(1, 8)] +
            [(i, -i) for i in range(1, 8)] +
            [(i, 0) for i in range(1, 8)] + 
            [(-i, 0) for i in range(1, 8)] + 
            [(0, i) for i in range(1, 8)] + 
            [(0, -i) for i in range(1, 8)]
        )


    def get_possible_moves(self):
        """Gathers all possible moves for the piece and stores them."""
        self.clear_moves()
        self.add_moves()


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
        self.moves = [
            (1, 0), (-1, 0), (0, 1), (0, -1), 
             (1, 1), (-1, -1), (-1, 1), (1, -1)
        ]
        super().__init__(color, surface_w, surface_b)


    def get_possible_moves(self):
        """Gathers all possible moves for the piece and stores them."""
        self.clear_moves()
        self.add_moves()