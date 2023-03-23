class Piece:
    """Define a class that describes a generic piece."""
    
    def __init__(self, x_coor, y_coor, color):

        # Denotes coordinates of the piece (0 - 7 in both dimentions)
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.color = color