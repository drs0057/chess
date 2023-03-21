import pygame
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from pawn import Pawn

# Notes:
# Rect class parameters: (abs. x_coor of top left corner, abs. y_coor of top left corner, width of rect, height of rect)
# pygame.draw.rect() parameters: (surface to draw on, color, object to draw)


# Intialize variables
light, dark = (237, 199, 190), (115, 88, 81)
width, height = 100, 100

class Square:
    """A class representing each square."""

    def __init__(self, x_coor, y_coor, screen):

        # Denotes coordinates of the square (0 - 7 in both dimentions)
        self.x_coor = x_coor
        self.y_coor = y_coor
        # Absolute positions of the top-left corner of the square
        self.x_abs = x_coor * width
        self.y_abs = y_coor * height
        # Define color
        self.color = light if (self.x_coor + self.y_coor) % 2 == 0 else dark
        # Screen to draw the square on
        self.screen = screen
        self.rect = pygame.Rect(self.x_abs, self.y_abs, width, height)
        self.occupying_piece = None

    # Method to draw individual square
    def draw(self):
        """Draws a square on the board and the potential piece occupying it."""

        pygame.draw.rect(self.screen, self.color, self.rect)
        if self.occupying_piece:
            rect = self.occupying_piece.image.get_rect(
                topleft = (self.x_abs, self.y_abs)
            )
            self.screen.blit(self.occupying_piece.image, rect)



class Board:
    """A class representing the board as a whole."""

    def __init__(self):

        # Initial state of the board's pieces; one list for each row
        self.init_state = [
            ['bR', 'bK', 'bB', 'bQ', 'bG', 'bB', 'bK', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wK', 'wB', 'wQ', 'wG', 'wB', 'wK', 'wR']
        ]

    def square_objects(self, screen):
        """Returns a 2D list of all 64 square objects."""
        squares = []
        for y_coor in range(8):
            row = []
            for x_coor in range(8):
                row.append(Square(x_coor, y_coor, screen))
            squares.append(row)
        return squares
    
    def initial_setup(self, squares):
        """Draws squares and places the pieces in their starting positions."""
        for y_coor, row in enumerate(self.init_state):
            for x_coor, piece in enumerate(row):
                
                if 'R' in piece:
                    color = 'w' if 'w' in piece else 'b'
                    squares[y_coor][x_coor].occupying_piece = Rook(
                        x_coor, y_coor, color
                    )

                if 'K' in piece:
                    color = 'w' if 'w' in piece else 'b'
                    squares[y_coor][x_coor].occupying_piece = Knight(
                        x_coor, y_coor, color
                    )

                if 'B' in piece:
                    color = 'w' if 'w' in piece else 'b'
                    squares[y_coor][x_coor].occupying_piece = Bishop(
                        x_coor, y_coor, color
                    )

                if 'Q' in piece:
                    color = 'w' if 'w' in piece else 'b'
                    squares[y_coor][x_coor].occupying_piece = Queen(
                        x_coor, y_coor, color
                    )

                if 'G' in piece:
                    color = 'w' if 'w' in piece else 'b'
                    squares[y_coor][x_coor].occupying_piece = King(
                        x_coor, y_coor, color
                    )

                if 'P' in piece:
                    color = 'w' if 'w' in piece else 'b'
                    squares[y_coor][x_coor].occupying_piece = Pawn(
                        x_coor, y_coor, color
                    )
            
        # All squares have corrected initial states, now display them
        for row in squares:
            for square in row:
                square.draw()