class Piece:
    """Define a class that describes a generic piece."""
    
    def __init__(self, color):

        self.color = color # Either 'w' or 'b'
        
        # Stores all possible moves, initially all False
        self.possible_moves = [
            [False for x_coor in range(8)] for y_coor in range(8)
        ]