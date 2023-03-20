import pygame

class Square:
    """A class representing each square."""

    # Initialize attributes
    def __init__(self, x_num, y_num, screen):

        # Denotes coordinates of the square (0 - 7 in both dimentions)
        self.x_num = x_num
        self.y_num = y_num
        # Absolute positions of the top-left corner of the square
        self.x_abs = x_num * 100
        self.y_abs = y_num * 100
        # Define color
        if (self.x_num + self.y_num) % 2 == 0:
            self.color = (237, 199, 190) # Light square
        elif self.x_num + self.y_num % 2 != 0:
            self.color = (115, 88, 81) # Dark square
        # Screen to draw the square on
        self.draw_screen = screen
        # Rect class parameters: (abs. x_coor of top left corner, 
        # abs. y_coor of top left corner, width of rect, height of rect)
        self.rect = pygame.Rect(self.x_abs, self.y_abs, 100, 100)

    # Method to draw individual square
    def draw(self):
        # pygame.draw.rect() parameters: (surface to draw on, color, 
        # object to draw)
        pygame.draw.rect(self.draw_screen, self.color, self.rect)



class Board:
    """A class representing the board as a whole."""

    # Initilaize attributes
    def __init__(self):
        self.placeholder = 1

    def build_square_objects(self, screen):
        """Returns a list of square objects."""
        squares = []
        for y_num in range(8):
            for x_num in range(8):
                squares.append(Square(x_num, y_num, screen))
        return squares
    
    def print_squares(self, squares):
        """Takes a list of square objects and prints them all. """
        for square in squares:
            square.draw()
        