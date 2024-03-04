This chess game is the final project for Harvard's CS50, an introduction to computer science.
This game is 100% written in Python and uses the PyGame library to aid in the drawing of objects and the flow of the game.

This project was meant to be an exercise in the practical application of object-oriented programming (OOP) principles.
OOP concepts like polymorphism, encapsulation, and inheritance served as the backbone for this project.
Below is a brief demo of the game in action:


https://github.com/drs0057/chess/assets/118777627/9f69ec16-c9c4-4b90-9de1-df677d29716f


### Game Objects/Logic
To efficiently and elegantly design a chess game, clever organizational techniques are required. This is where OOP shines. 

The objects in this game were designed hierarchically. The defining structures were:
- The "Board" class, which controls all squares and tracks the state of the game. This includes setting up the board, selecting squares, and switching turns.
- The "Square" class, which tracks the state of a single square, including whether it is selected and what piece it contains. Square objects are passed back in forth in many methods of the "Board" class.
- The "Piece" class, which describes a generic piece. This object tracks the type of piece, the square it resides in, whether it has moved, etc.
- Individual piece classes, where each unique type of piece has a class that tracks several things, the most important being an array of legal moves for that piece.

Below is a simple diagram that visualizes this hierarchy:

<div align="center">
  <img src="media/logic_structure" alt="Visual of the logic structure" style="width:50%;">
</div>

This robust structure of objects allows for a fast query of whatever board state is needed. After each move, the board is scanned and each piece updates its list of legal moves. 
Pieces are handed off seamlessly from square to square, and changes are quickly reflected on the screen as PyGame helps to draw the new changes on the board.

A simple while loop controls the flow of the game. A timer counts down the clock for the appropriate player, all while the Board object keeps track of whose turn it is, the state of the game, etc. 

### Lessons Learned
- The application of good OOP principles was an overall success in this project, but it was far from perfect. Some OOP principles failed to make an appearance, causing some headaches as the codebase grew. For example, a lack of encapsulation in some methods of the Board class created clustered and confusing code in other methods. Some logic did not need to extend beyond its home method, and yet was being tracked/checked across multiple other methods.
- I failed to make a robust sketch of the class structure before writing code. The present class structure emerged as a result of the problems I was having while coding. This logical flow is the opposite of what should be done. I should have outlined a comprehensive design for the objects that I needed BEFORE writing any code. This would have saved much of the time that I spent haphazardly wandering across different methods trying to chain together their logic.


