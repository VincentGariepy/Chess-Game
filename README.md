# Chess-Game
Chess game built from scratch using the pygame library. This was a project to help improve my Python coding abilities, mainly in OOP. The code creates a chess board with a random color assigned at the bottom, white is always first to play. To play simply click on the piece you wish to move and the highlighted green squares will be all the possible moves for this piece. The code makes sure you do not play an illegal move. All rules of chess are included in this version i.e. en passant, castling (both sides), promoting to a queen. A game will end by either stalemate or checkmate.
On the right of the screen all moves will be printed out in standard algebraic notation, when the player clicks on this part of the screen a .txt file will be created with the notation exported as a pgn (Portable Game Notation) standard so it can be put into any chess engine or website to be analysed.

To run the code simply put the the files ChessGame.py, ChessClasses.py and the folder Chess_pieces into a common folder. Simply running the ChessGame.py file should start up the game in another window. 

Libraries needed :
-pygame
-math
-sys
-random
-numpy
-fnmatch
