#Attempt at chess game
#June 3rd 2021 
#This is the main script to run the game, you must have ChessClasses.py in the same folder then you can run this
#It will open a different window with the game
import pygame as pygame

from ChessClasses import Board

pygame.init()
 
size = width, height = 512+64*4, 512+64*2
white = 255,233,197
clear_white = 255,255,255
black = 87, 58, 46
grey = 135,  135, 135
highlight = 192, 192, 192
check = 255, 0, 0
move= 175, 255, 200
title = "First Chess Game"
    
width = 64 # width of the square
original_color = ''

GameBoard = Board(size,white,clear_white,black,grey,highlight,check,move,title,width,original_color)

GameBoard.board_setup()

GameBoard.create_pieces()
 
GameBoard.create_board()

GameBoard.add_pieces()

GameBoard.play()

        
    
    
    