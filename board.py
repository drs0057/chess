import pygame

class Square:
    """A class representing each square."""

    # Initialize attributes
    def __init__(self, x, y, color):
        
        # Absolute positions of the top-left corner
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
        self.pos_size = (x, y, self.width, self.height)
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

