import pygame

# Intialize variables
light, dark = (237, 199, 190), (115, 88, 81)
width, height = 100, 100

class Square:
    """A class representing each square."""

    # Initialize attributes
    def __init__(self, x_num, y_num, screen):

        # Denotes coordinates of the square (0 - 7 in both dimentions)
        self.x_num = x_num
        self.y_num = y_num
        # Absolute positions of the top-left corner of the square
        self.x_abs = x_num * width
        self.y_abs = y_num * height
        # Define color
        self.color = light if (self.x_num + self.y_num) % 2 == 0 else dark
        # Screen to draw the square on
        self.screen = screen
        # Rect class parameters: (abs. x_coor of top left corner, 
        # abs. y_coor of top left corner, width of rect, height of rect)
        self.rect = pygame.Rect(self.x_abs, self.y_abs, width, height)

        self.occupying_piece = None

    # Method to draw individual square
    def draw(self):
        """Draws the sqaure on the board."""
        # pygame.draw.rect() parameters: (surface to draw on, color, 
        # object to draw)
        pygame.draw.rect(self.screen, self.color, self.rect)
        # Checks if a piece is on the square
        if self.occupying_piece:
            rect = self.occupying_piece.image.get_rect(topleft = (0,0))
            self.screen.blit(self.occupying_piece.image, rect)



class Board:
    """A class representing the board as a whole."""

    # Initilaize attributes
    def __init__(self):

        # State of the board's pieces; one list for each row
        self.init_state = [
            ['bR', 'bK', 'bB', 'bQ', 'bG', 'bB', 'bK', 'bR']
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP']
            ['', '', '', '', '', '', '', '']
            ['', '', '', '', '', '', '', '']
            ['', '', '', '', '', '', '', '']
            ['', '', '', '', '', '', '', '']
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP']
            ['wR', 'wK', 'wB', 'wQ', 'wG', 'wB', 'wK', 'wR']
        ]

    def build_square_objects(self, screen):
        """Returns a list of all 64 square objects."""
        squares = []
        for y_num in range(8):
            for x_num in range(8):
                squares.append(Square(x_num, y_num, screen))
        return squares
    
    def print_squares(self, squares):
        """Takes a list of square objects and draws them on the board. """
        for square in squares:
            square.draw()
    
    def initial_setup(self, squares):
        """Places the pieces in their starting positions."""
        for square in squares:
            square.occupying_piece = 'wB'