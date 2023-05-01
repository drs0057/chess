import pygame
from variables import total_time, player_1_location, player_2_location, height, width, x_offset, y_offset, x_labels, y_labels, light, dark, initial_state, test_state, select_color, background_color
from pieces import Pawn, Knight, Bishop, Rook, Queen, King

# Notes:

# Rect class parameters: (abs. x_coor of top left corner, abs. y_coor of top left corner, width of rect, height of rect)
# pygame.draw.rect() parameters: (surface to draw on, color, object to draw)

# When square is clicked: ---> click() ---> get_square_from_abs() ---> select_clicked_square() or find_selected_square() ---> move_piece()


class Player:
    """A class describing one of the players."""
    def __init__(self, color):
        self.color = color # Either 'w' or 'b'
        self.is_turn = False
        self.time_remaining_ms = total_time
        self.text_location = player_1_location if color == 'w' else player_2_location
        self.last_time = 0



class Square:
    """A class representing each square."""

    def __init__(self, x_coor, y_coor, screen):
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.x_abs = x_coor * width + x_offset
        self.y_abs = y_coor * height + y_offset
        self.occupying_piece = None
        self.is_selected = False
        self.color = light if (self.x_coor + self.y_coor) % 2 == 0 else dark
        self.display_color = self.color
        self.screen = screen
        self.rect = pygame.Rect(self.x_abs, self.y_abs, width, height)


    def draw(self):
        """Draws a square on the board and the potential piece occupying it."""
        # Draw the basic square
        pygame.draw.rect(self.screen, self.display_color, self.rect)
        # Draw the piece occupying the square, if there is one
        if self.occupying_piece:
            piece_rect = self.occupying_piece.image.get_rect(
                topleft = (self.x_abs, self.y_abs)
            )
            self.screen.blit(self.occupying_piece.image, piece_rect)



class Board:
    """A class representing the board as a whole."""
    def __init__(self, screen):
        self.init_state = test_state
        self.squares = None
        self.build_square_objects(screen)
        self.board_square_selected = False
        self.screen = screen
        self.first_move = False
        self.player1 = Player('w')
        self.player2 = Player('b')
        self.current_player = self.player1
        self.total_time = total_time


    def build_square_objects(self, screen):
        """Assigns an attribute; a 2D list of all 64 square objects."""

        squares = []
        for y_coor in range(8):
            row = []
            for x_coor in range(8):
                row.append(Square(x_coor, y_coor, screen))
            squares.append(row)
        self.squares = squares


    def click(self, x_abs, y_abs):
        """Handles any click event that is detected."""

        clicked_square = self.get_square_from_abs(x_abs, y_abs)

        # Situation 1: No square is currently selected;
        # select the clicked square
        if self.board_square_selected == False and clicked_square != None:
            self.select_square(clicked_square)

        # Situation 2: A square with a piece on it is already selected
        elif self.board_square_selected == True and clicked_square != None:

            # Find the square that is currently selected
            current_square = self.find_selected_square()
                
            # Check for castle
            if type(current_square.occupying_piece).__name__ == 'King' \
            and type(clicked_square.occupying_piece).__name__ == 'Rook':
                self.castle(current_square, clicked_square)
                return

            # Check for promotion
            if type(current_square.occupying_piece).__name__ == 'Pawn' and \
            clicked_square.y_coor in [0, 7]:
                self.promote(current_square, clicked_square)

            # Situation 2b: A piece occupies the clicked square
            elif clicked_square.occupying_piece:
                # Like colors cannot capture
                if self.current_player.color == clicked_square.occupying_piece.color:
                    self.select_square(clicked_square)
                    return
                else:
                    self.move_piece(current_square, clicked_square)

            # Situation 2c: Clicked square is empty
            else:
                self.move_piece(current_square, clicked_square)


    def castle(self, king_square1, rook_square1):
        """Castles the king and the rook. Must have standalone logic 
        since castling breaks traditional legality checks."""

        # If either piece has moved, cancel the castle
        if king_square1.occupying_piece.has_moved \
            or rook_square1.occupying_piece.has_moved:
            self.select_square(rook_square1)
            return        
        
        # Castle to the  right
        if king_square1.x_coor < rook_square1.x_coor:

            # If path is not clear, cancel the castle
            for i in [1, 2]:
                if self.squares[king_square1.y_coor][king_square1.x_coor + i].occupying_piece:
                    self.select_square(rook_square1)
                    return

            # Move King
            king_square2 = self.squares[king_square1.y_coor][king_square1.x_coor + 2]
            moving_king = king_square1.occupying_piece
            moving_king.has_moved = True
            king_square1.occupying_piece = None
            king_square2.occupying_piece = moving_king
            king_square1.draw()
            king_square2.draw()

            # Move Rook
            rook_square2 = self.squares[king_square2.y_coor][king_square2.x_coor - 1]
            moving_rook = rook_square1.occupying_piece
            moving_rook.has_moved = True
            rook_square1.occupying_piece = None
            rook_square2.occupying_piece = moving_rook
            rook_square1.draw()
            rook_square2.draw()

            self.end_turn()
        
        # Castle to the left
        elif king_square1.x_coor > rook_square1.x_coor:

           # If path is not clear, cancel the castle
            for i in [1, 2, 3]:
                if self.squares[king_square1.y_coor][king_square1.x_coor - i].occupying_piece:
                    self.select_square(rook_square1)
                    return
                            
            # Move King
            king_square2 = self.squares[king_square1.y_coor][king_square1.x_coor - 2]
            moving_king = king_square1.occupying_piece
            moving_king.has_moved = True
            king_square1.occupying_piece = None
            king_square2.occupying_piece = moving_king
            king_square1.draw()
            king_square2.draw()

            # Move Rook
            rook_square2 = self.squares[king_square2.y_coor][king_square2.x_coor + 1]
            moving_rook = rook_square1.occupying_piece
            moving_rook.has_moved = True
            rook_square1.occupying_piece = None
            rook_square2.occupying_piece = moving_rook
            rook_square1.draw()
            rook_square2.draw()

            self.end_turn()


    def deselect_square(self, square):
        """Takes in a square object and 'deselects' it."""
        
        square.is_selected = False
        square.display_color = square.color
        square.draw()
        self.board_square_selected = False

    
    def end_turn(self):
        """Ends the turn of the current player."""

        # Deselect the previous square
        self.deselect_square(self.find_selected_square())

        # Refresh possible moves across the whole board
        self.refresh_possible_board_moves()

        # Switch players
        self.switch_turn()


    def find_selected_square(self):
        """Returns the square object that is currently selected, returns
        none if there isn't one."""

        for row in self.squares:
            for square in row:
                if square.is_selected:
                    return square
        return None


    def get_square_from_abs(self, x_abs, y_abs):
        """Take absolute x and y position, returns corresponding square 
        object."""

        # Determine which coordinate was clicked
        x_coor = int((x_abs - x_offset) // width)
        y_coor = int((y_abs - y_offset) // height)

        if x_coor not in range(8) or y_coor not in range(8):
            return None
        else:
            square = self.squares[y_coor][x_coor]
            return square


    def initial_setup(self):
        """Draws squares and places the pieces in their starting positions.
        Also writes needed text."""

        for y_coor, row in enumerate(self.init_state):
            for x_coor, piece in enumerate(row):
                
                if 'R' in piece:
                    color = 'w' if 'w' in piece else 'b'
                    square = self.squares[y_coor][x_coor]
                    square.occupying_piece = Rook(color)
                    square.occupying_piece.residing_square = square

                if 'K' in piece:
                    color = 'w' if 'w' in piece else 'b'
                    square = self.squares[y_coor][x_coor]
                    square.occupying_piece = Knight(color)
                    square.occupying_piece.residing_square = square

                if 'B' in piece:
                    color = 'w' if 'w' in piece else 'b'
                    square = self.squares[y_coor][x_coor]
                    square.occupying_piece = Bishop(color)
                    square.occupying_piece.residing_square = square

                if 'Q' in piece:
                    color = 'w' if 'w' in piece else 'b'
                    square = self.squares[y_coor][x_coor]
                    square.occupying_piece = Queen(color)
                    square.occupying_piece.residing_square = square

                if 'G' in piece:
                    color = 'w' if 'w' in piece else 'b'
                    square = self.squares[y_coor][x_coor]
                    square.occupying_piece = King(color)
                    square.occupying_piece.residing_square = square

                if 'P' in piece:
                    color = 'w' if 'w' in piece else 'b'
                    square = self.squares[y_coor][x_coor]
                    square.occupying_piece = Pawn(color)
                    square.occupying_piece.residing_square = square
            
        # All squares have corrected initial states, now display them
        for row in self.squares:
            for square in row:
                square.draw()

        # Refresh possible moves across the whole board
        self.refresh_possible_board_moves()
        
        # Display all needed text
        self.write_coordinates()
        self.write_player_names()
        self.write_starting_times()


    def is_legal(self, current_square, clicked_square):
        """Checks if a move is legal, returns boolean."""
        if current_square.occupying_piece.possible_moves[clicked_square.y_coor]\
        [clicked_square.x_coor] == True:
            return True
        else:
            return False

   
    def move_piece(self, current_square, clicked_square):
        """Moves a piece from one square to another. Legality is checked."""
        if self.is_legal(current_square, clicked_square):
            moving_piece = current_square.occupying_piece
            moving_piece.has_moved = True
            current_square.occupying_piece = None
            clicked_square.occupying_piece = moving_piece
            clicked_square.occupying_piece.residing_square = clicked_square
            current_square.draw()
            clicked_square.draw()
            self.end_turn()
        else:
            self.deselect_square(current_square)


    def promote(self, current_square, clicked_square):
        """Promotes a pawn to a queen."""
        if self.is_legal(current_square, clicked_square):
            clicked_square.occupying_piece = Queen(current_square.occupying_piece.color)
            clicked_square.occupying_piece.residing_square = clicked_square
            current_square.occupying_piece = None
            current_square.draw()
            clicked_square.draw()
            self.end_turn()
        else:
            self.deselect_square(current_square)


    def refresh_possible_board_moves(self):
        """Refreshes each piece's possible moves."""

        for row in self.squares:
            for square in row:
                if square.occupying_piece:
                    square.occupying_piece.get_possible_moves(self.squares)


    def select_square(self, square):
        """Takes in a square object. 'Deselects' previous square if 
        there is one, 'selects' desired square."""

        # Deselect previous square selected if there is one
        prev_square = self.find_selected_square()
        if prev_square:
            self.deselect_square(prev_square)
    
        # Check if piece is occupying the square and check for current player
        if square.occupying_piece:

            if self.current_player.color == square.occupying_piece.color:
                square.is_selected = True
                square.display_color = select_color
                square.draw()
                self.board_square_selected = True


    def switch_turn(self):
        """Switches turns."""

        # Switch players
        # self.current_player = self.player2 if self.current_player == self.player1 else self.player1

        # Log the current time
        self.current_player.last_time = pygame.time.get_ticks()

        # Indicate if first move has occured
        if self.first_move == False:
            self.first_move = True


    def timer(self, player, screen):
        """Takes in a player object and counts down their time."""
        font = pygame.font.SysFont("Arial", 30)
        if self.first_move:
            # Count down the time
            elapsed_time = pygame.time.get_ticks() - self.current_player.last_time
            player.time_remaining_ms -= elapsed_time
            minutes = (player.time_remaining_ms // 1000) // 60
            seconds = (player.time_remaining_ms // 1000) % 60            
            time_format = "{:02d}:{:02d}".format(minutes, seconds)
            time_text = font.render(time_format, False, (0, 0, 0))

            # Cover up the last time, then display new time
            cover_up_rect = pygame.Rect(
                player.text_location[0] + 125, player.text_location[1], 100, 30
                )
            pygame.draw.rect(screen, background_color, cover_up_rect)
            self.screen.blit(
                time_text, 
                (player.text_location[0] + 135, player.text_location[1])
                )

            # Note what the current time is
            self.current_player.last_time = pygame.time.get_ticks()


    def write_coordinates(self):
        """Writes all coordinate labels."""

        font = pygame.font.SysFont("Arial", 28)
        for x_coor in range(8):
            self.screen.blit(
                (font.render(x_labels[x_coor], True, (0, 0, 0))), 
                ((x_coor * width) + x_offset + width/2 - 5, y_offset + height*8 + 3)
            )

        for y_coor in range(8):
            self.screen.blit(
                (font.render(y_labels[y_coor], True, (0, 0, 0))), 
                (x_offset - 20, y_coor * height + y_offset + height/2 - 8)
            )

        
    def write_player_names(self):
        """Writes both player names."""

        # Write player names
        font = pygame.font.SysFont("Arial", 28, bold=True)
        self.screen.blit(
            font.render("Player 2:", True, (0, 0, 0)),
            (self.player2.text_location)
        )

        self.screen.blit(
            font.render("Player 1:", True, (0, 0, 0)),
            (self.player1.text_location)
        )


    def write_starting_times(self):
        """Writes both starting times"""
        
        font = pygame.font.SysFont("Arial", 30)
        minutes = (self.total_time // 1000) // 60
        seconds = (self.total_time // 1000) % 60            
        time_format = "{:02d}:{:02d}".format(minutes, seconds)
        time_text = font.render(time_format, False, (0, 0, 0))
        self.screen.blit(
            time_text, 
            (self.player1.text_location[0] + 135, 
             self.player1.text_location[1])
            )
        self.screen.blit(
            time_text, 
            (self.player2.text_location[0] + 135, 
             self.player2.text_location[1])
            )