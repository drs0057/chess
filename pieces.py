import pygame
from variables import width, height

class Piece:
    """Define a class that describes a generic piece."""
    def __init__(self, color, surface_w, surface_b):
        self.color = color  # Either 'w' or 'b'
        self.has_moved = False
        self.residing_square = None
        self.possible_moves = None
        # Determine image based on the color
        self.image = surface_w if color == 'w' else surface_b
        # All possible moves initialized to False
        self.clear_moves()

    
    def clear_moves(self):
        """Resets a piece's moves and possible moves."""
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
        self.moves = [(-1, 0), (-2, 0)]
        super().__init__(color, surface_w, surface_b)


    def get_possible_moves(self, squares):
        """Gathers all moves for the piece."""
        self.clear_moves()
        if self.color == 'w':
            self.add_moves_until_blocked(-1, 0, squares)
        elif self.color == 'b':
            self.add_moves_until_blocked(1, 0, squares)


    def add_moves_until_blocked(self, y_dir, x_dir, squares):
        """Adds moves to piece's possible moves if the move is not blocked."""
        new_y = self.residing_square.y_coor + y_dir
        new_x = self.residing_square.x_coor + x_dir
        if new_y in range(8) and new_x in range(8) and \
            squares[new_y][new_x].occupying_piece == None:
            self.possible_moves[new_y][new_x] = True

        # Check for diagonally taking a piece
        if new_x - 1 in range(8):
            if squares[new_y][new_x - 1].occupying_piece is not None:
                self.possible_moves[new_y][new_x - 1] = True
        if new_x + 1 in range(8):
            if squares[new_y][new_x + 1].occupying_piece is not None:
                self.possible_moves[new_y][new_x + 1] = True
        
        # Check for initial pawn move
        if self.has_moved == False:
            for i in range(1, 3):
                new_y = self.residing_square.y_coor + y_dir * i
                new_x = self.residing_square.x_coor + x_dir * i
                if new_y not in range(8) or new_x not in range(8) or \
                    squares[new_y][new_x].occupying_piece is not None:
                    return
                self.possible_moves[new_y][new_x] = True



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


    def get_possible_moves(self, squares):
        """Gathers all moves for the piece."""
        self.clear_moves()
        self.add_moves_until_blocked(-2, -1, squares)
        self.add_moves_until_blocked(-2, 1, squares)
        self.add_moves_until_blocked(2, -1, squares)
        self.add_moves_until_blocked(2, 1, squares)
        self.add_moves_until_blocked(-1, -2, squares)
        self.add_moves_until_blocked(-1, 2, squares)
        self.add_moves_until_blocked(1, -2, squares)
        self.add_moves_until_blocked(1, 2, squares)


    def add_moves_until_blocked(self, y_dir, x_dir, squares):
        """Adds moves to piece's possible moves if the move is not blocked."""
        new_y = self.residing_square.y_coor + y_dir
        new_x = self.residing_square.x_coor + x_dir
        if new_y not in range(8) or new_x not in range(8):
            return
        self.possible_moves[new_y][new_x] = True



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


    def get_possible_moves(self, squares):
        """Gathers all moves for the piece."""
        self.clear_moves()
        self.add_moves_until_blocked(1, 1, squares)
        self.add_moves_until_blocked(1, -1, squares)
        self.add_moves_until_blocked(-1, 1, squares)
        self.add_moves_until_blocked(-1, -1, squares)


    def add_moves_until_blocked(self, y_dir, x_dir, squares):
        """Adds moves to piece's possible moves if the move is not blocked."""
        for i in range(1, 8):
            new_y = self.residing_square.y_coor + i * y_dir
            new_x = self.residing_square.x_coor + i * x_dir
            if new_y not in range(8) or new_x not in range(8):
                continue
            self.possible_moves[new_y][new_x] = True
            if squares[new_y][new_x].occupying_piece:
                break



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


    def get_possible_moves(self, squares):
        """Gathers all moves for the piece."""
        self.clear_moves()
        self.add_moves_until_blocked(0, 1, squares)
        self.add_moves_until_blocked(0, -1, squares)
        self.add_moves_until_blocked(1, 0, squares)
        self.add_moves_until_blocked(-1, 0, squares)


    def add_moves_until_blocked(self, y_dir, x_dir, squares):
        """Adds moves to piece's possible moves if the move is not blocked."""
        for i in range(1, 8):
            new_y = self.residing_square.y_coor + i * y_dir
            new_x = self.residing_square.x_coor + i * x_dir
            if new_y not in range(8) or new_x not in range(8):
                continue
            self.possible_moves[new_y][new_x] = True
            if squares[new_y][new_x].occupying_piece:
                break



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


    def get_possible_moves(self, squares):
        """Gathers all moves for the piece."""
        self.clear_moves()
        self.add_moves_until_blocked(0, 1, squares)
        self.add_moves_until_blocked(0, -1, squares)
        self.add_moves_until_blocked(1, 0, squares)
        self.add_moves_until_blocked(-1, 0, squares)
        self.add_moves_until_blocked(1, 1, squares)
        self.add_moves_until_blocked(1, -1, squares)
        self.add_moves_until_blocked(-1, 1, squares)
        self.add_moves_until_blocked(-1, -1, squares)


    def add_moves_until_blocked(self, y_dir, x_dir, squares):
        """Adds moves to piece's possible moves if the move is not blocked."""
        for i in range(1, 8):
            new_y = self.residing_square.y_coor + i * y_dir
            new_x = self.residing_square.x_coor + i * x_dir
            if new_y not in range(8) or new_x not in range(8):
                continue
            self.possible_moves[new_y][new_x] = True
            if squares[new_y][new_x].occupying_piece:
                break



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


    def get_possible_moves(self, squares):
        """Gathers all moves for the piece."""
        self.clear_moves()
        self.add_moves_until_blocked(0, 1, squares)
        self.add_moves_until_blocked(0, -1, squares)
        self.add_moves_until_blocked(1, 0, squares)
        self.add_moves_until_blocked(-1, 0, squares)
        self.add_moves_until_blocked(1, 1, squares)
        self.add_moves_until_blocked(1, -1, squares)
        self.add_moves_until_blocked(-1, 1, squares)
        self.add_moves_until_blocked(-1, -1, squares)


    def add_moves_until_blocked(self, y_dir, x_dir, squares):
        """Adds moves to piece's possible moves if the move is not blocked."""
        new_y = self.residing_square.y_coor + y_dir
        new_x = self.residing_square.x_coor + x_dir
        if new_y not in range(8) or new_x not in range(8):
            return
        self.possible_moves[new_y][new_x] = True