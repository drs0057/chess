import pygame
from variables import *
from pieces import *

# Notes:

# Rect class parameters: (abs. x_coor of top left corner, abs. y_coor of top left corner, width of rect, height of rect)
# pygame.draw.rect() parameters: (surface to draw on, color, object to draw)

# When square is clicked: ---> click() ---> get_square_from_coor() ---> select_clicked_square() or find_selected_square() ---> move_piece()


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
        self.init_state = initial_state
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

        clicked_square = self.get_square_from_coor(x_abs, y_abs)

        # Situation 1: No square is currently selected;
        # select the clicked square
        if self.board_square_selected == False and clicked_square != None:
            self.select_square(clicked_square)

        # Situation 2: A square with a piece on it is already selected
        elif self.board_square_selected == True and clicked_square != None:

            # Find the square that is currently selected
            current_square = self.find_selected_square()

            # Situation 2a: Move piece to empty square
            if clicked_square.occupying_piece == None:
                self.move_piece(current_square, clicked_square)

            # Situation 2b: A piece is on the target square
            else:
              self.selected_piece_to_occupied_square(
                  current_square, clicked_square
                  )


    def deselect_square(self, square):
        """Takes in a square object and 'deselects' it."""
        
        square.is_selected = False
        square.display_color = square.color
        square.draw()
        self.board_square_selected = False


    def find_selected_square(self):
        """Returns the square object that is currently selected, returns
        none if there isn't one."""

        for row in self.squares:
            for square in row:
                if square.is_selected:
                    return square
        return None


    def get_square_from_coor(self, x_abs, y_abs):
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
                    self.squares[y_coor][x_coor].occupying_piece = Rook(color)

                if 'K' in piece:
                    color = 'w' if 'w' in piece else 'b'
                    self.squares[y_coor][x_coor].occupying_piece = Knight(color)

                if 'B' in piece:
                    color = 'w' if 'w' in piece else 'b'
                    self.squares[y_coor][x_coor].occupying_piece = Bishop(color)

                if 'Q' in piece:
                    color = 'w' if 'w' in piece else 'b'
                    self.squares[y_coor][x_coor].occupying_piece = Queen(color)

                if 'G' in piece:
                    color = 'w' if 'w' in piece else 'b'
                    self.squares[y_coor][x_coor].occupying_piece = King(color)

                if 'P' in piece:
                    color = 'w' if 'w' in piece else 'b'
                    self.squares[y_coor][x_coor].occupying_piece = Pawn(color)
            
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


    def move_piece(self, current_square, target_square):
        """Takes in the current square and the target square objects, 
        displays the outcome of the move."""

        moving_piece = current_square.occupying_piece
        # Clear the previous square
        current_square.occupying_piece = None
        # Move the piece to the target square
        target_square.occupying_piece = moving_piece
        # Redraw both squares
        current_square.draw()
        target_square.draw()
        
        # Deselect the previous square
        self.deselect_square(current_square)

        # Refresh possible moves across the whole board
        self.refresh_possible_board_moves()

        # Switch players
        self.switch_turn()


    def refresh_possible_board_moves(self):
        """Refreshes each piece's possible moves."""

        for row in self.squares:
            for square in row:
                if square.occupying_piece:
                    square.occupying_piece.get_possible_moves()


    def select_square(self, square):
        """Takes in a square object. 'Deselects' previous square if 
        there is one, 'selects' desired square."""

        # Deselect previous square selected if there is one
        prev_square = self.find_selected_square()
        if prev_square:
            self.deselect_square(prev_square)
    
        # Check if piece is occupying the square and check for current player
        if square.occupying_piece:

            if self.current_player.color == 'w':
                if square.occupying_piece.color == 'w':
                    square.is_selected = True
                    square.display_color = select_color
                    square.draw()
                    self.board_square_selected = True

            elif self.current_player.color == 'b':
                    if square.occupying_piece.color == 'b':
                        square.is_selected = True
                        square.display_color = select_color
                        square.draw()
                        self.board_square_selected = True


    def selected_piece_to_occupied_square(self, current_square, clicked_square):
        """Deals with a selected piece potentially traveling to an 
        occupied square."""

        if self.current_player.color == 'w':
            # Check for castle first
            if type(current_square.occupying_piece).__name__ == 'King' \
                and type(clicked_square.occupying_piece).__name__ == 'Rook':
                self.move_piece(current_square, clicked_square)
            elif clicked_square.occupying_piece.color == 'b':
                self.move_piece(current_square, clicked_square)
            else:
                self.deselect_square(current_square)

        elif self.current_player.color == 'b':
            # Check for castle first
            if type(current_square.occupying_piece).__name__ == 'King' \
                and type(clicked_square.occupying_piece).__name__ == 'Rook':
                self.move_piece(current_square, clicked_square)
            elif clicked_square.occupying_piece.color == 'w':
                self.move_piece(current_square, clicked_square)
            else:
                self.deselect_square(current_square)


    def switch_turn(self):
        """Switches turns."""

        # Switch players
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

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