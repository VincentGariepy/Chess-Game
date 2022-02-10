#Classes for chess

import pygame as pygame

import math

import sys

import random

import numpy as geek

import fnmatch

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('Times New Roman', 50)
myfont_notation = pygame.font.SysFont('Times New Roman', 25)
myfont_board = pygame.font.SysFont('arial', 20)

#These are the classes for the pieces, some attributes are set when initialized, others stay empty until needed
class Knight:
    value = 3
    def __init__(self, position, color, image, name):
        self.position = position
        self.color = color
        self.image = image    
        self.name = name
        self.can_move = [[]]
        self.can_move.clear()
        self.does_protect = [[]]
        self.does_protect.clear()
        self.move_not_eat = [[]]
        self.move_not_eat.clear() 
        
class Bishop:
    value = 3
    def __init__(self, position, color, image, name):
        self.position = position
        self.color = color
        self.image = image
        self.name = name
        self.can_move = [[]]
        self.can_move.clear()
        self.does_protect = [[]]
        self.does_protect.clear()
        self.move_not_eat = [[]]
        self.move_not_eat.clear() 
        
class Rook:
    value = 5
    def __init__(self, position, color, image, name):
        self.position = position
        self.color = color
        self.image = image
        self.name = name
        self.can_move = [[]]
        self.can_move.clear()
        self.does_protect = [[]]
        self.does_protect.clear()
        self.move_not_eat = [[]]
        self.move_not_eat.clear() 
        
class Queen:
    value = 9
    def __init__(self, position, color, image, name):
        self.position = position
        self.color = color
        self.image = image
        self.name = name
        self.can_move = [[]]
        self.can_move.clear()
        self.does_protect = [[]]
        self.does_protect.clear()  
        self.move_not_eat = [[]]
        self.move_not_eat.clear() 
             
class King:
    value = 0
    def __init__(self, position, color, image, name):
        self.position = position
        self.color = color
        self.image = image
        self.name = name
        self.can_move = [[]]
        self.can_move.clear()
        self.does_protect = [[]]
        self.does_protect.clear()
        self.move_not_eat = [[]]
        self.move_not_eat.clear()         
        
class Pawn:
    value = 1
    def __init__(self, position, color, image, name):
        self.position = position
        self.color = color
        self.image = image
        self.name = name
        self.can_move = [[]]
        self.can_move.clear()
        self.does_protect = [[]]
        self.does_protect.clear()
        self.move_not_eat = [[]]
        self.move_not_eat.clear()        


#This is the board class, it is where all the functions are to play the game 
class Board:
    #Initialize values
    click = [-1,-1]
    turn = 1
    selected_piece = None
    previously_selected = None
    king_check = None
    nbr_queens_w = 0
    nbr_queens_b = 0
    can_castle_long_w = True
    can_castle_long_b = True
    can_castle_short_w = True
    can_castle_short_b = True
    textgame_string = ''
    textgame = myfont_notation.render(textgame_string, 0, (255,255,255))
    en_passant = None
    result = ''
    
    
    def __init__(self, size, white, clear_white, black, grey, highlight, red, move_color, title, width, original_color):
        self.size = size
        self.white = white
        self.clear_white = clear_white
        self.black = black
        self.grey = grey
        self.highlight = highlight
        self.red = red
        self.move_color = move_color
        self.title = title
        self.width = width
        self.original_color = original_color
    
    #This function builds the board virtually, placing each piece in a matrix to keep track of position
    #Random number to get if white or black is at bottom
    def board_setup(self):
        r = random.randint(1,2)
        if(r == 1):
            self.board_pieces = [['br1','bp1',None,None,None,None,'wp1','wr1'],
                    ['bn1','bp2',None,None,None,None,'wp2','wn1'],
                    ['bb1','bp3',None,None,None,None,'wp3','wb1'],
                    ['bq','bp4',None,None,None,None,'wp4','wq'],
                    ['bk','bp5',None,None,None,None,'wp5','wk'],
                    ['bb2','bp6',None,None,None,None,'wp6','wb2'],
                    ['bn2','bp7',None,None,None,None,'wp7','wn2'],
                    ['br2','bp8',None,None,None,None,'wp8','wr2']
                    ]
            self.start = 'white'
            self.second = 'black'
            self.top = 'black'
        else:
            self.board_pieces = [['wr1','wp1',None,None,None,None,'bp1','br1'],
                    ['wn1','wp2',None,None,None,None,'bp2','bn1'],
                    ['wb1','wp3',None,None,None,None,'bp3','bb1'],
                    ['wk','wp4',None,None,None,None,'bp4','bk'],
                    ['wq','wp5',None,None,None,None,'bp5','bq'],
                    ['wb2','wp6',None,None,None,None,'bp6','bb2'],
                    ['wn2','wp7',None,None,None,None,'bp7','bn2'],
                    ['wr2','wp8',None,None,None,None,'bp8','br2']
                    ]
            self.start = 'white'
            self.second = 'black'
            self.top = 'white'      
        
    #This function creates all the pieces from the classes, loads image and position
    def create_pieces(self):
            
        self.br1 = Rook([self.get_place('br1')[0],self.get_place('br1')[1]],'black','Chess_pieces\BlackRook.png','br1')
        self.br2 = Rook([self.get_place('br2')[0],self.get_place('br2')[1]],'black','Chess_pieces\BlackRook.png','br2')
        self.wr1 = Rook([self.get_place('wr1')[0],self.get_place('wr1')[1]],'white','Chess_pieces\WhiteRook.png','wr1')
        self.wr2 = Rook([self.get_place('wr2')[0],self.get_place('wr2')[1]],'white','Chess_pieces\WhiteRook.png','wr2')
        
        self.bb1 = Bishop([self.get_place('bb1')[0],self.get_place('bb1')[1]],'black','Chess_pieces\BlackBishop.png','bb1')
        self.bb2 = Bishop([self.get_place('bb2')[0],self.get_place('bb2')[1]],'black','Chess_pieces\BlackBishop.png','bb2')
        self.wb1 = Bishop([self.get_place('wb1')[0],self.get_place('wb1')[1]],'white','Chess_pieces\WhiteBishop.png','wb1')
        self.wb2 = Bishop([self.get_place('wb2')[0],self.get_place('wb2')[1]],'white','Chess_pieces\WhiteBishop.png','wb2')
        
        self.bn1 = Knight([self.get_place('bn1')[0],self.get_place('bn1')[1]],'black','Chess_pieces\BlackKnight.png','bn1')
        self.bn2 = Knight([self.get_place('bn2')[0],self.get_place('bn2')[1]],'black','Chess_pieces\BlackKnight.png','bn2')
        self.wn1 = Knight([self.get_place('wn1')[0],self.get_place('wn1')[1]],'white','Chess_pieces\WhiteKnight.png','wn1')
        self.wn2 = Knight([self.get_place('wn2')[0],self.get_place('wn2')[1]],'white','Chess_pieces\WhiteKnight.png','wn2')
        
        self.bq = Queen([self.get_place('bq')[0],self.get_place('bq')[1]],'black','Chess_pieces\BlackQueen.png', 'bq')
        self.bk = King([self.get_place('bk')[0],self.get_place('bk')[1]],'black','Chess_pieces\BlackKing.png', 'bk')
        self.wq = Queen([self.get_place('wq')[0],self.get_place('wq')[1]],'white','Chess_pieces\WhiteQueen.png', 'wq')
        self.wk = King([self.get_place('wk')[0],self.get_place('wk')[1]],'white','Chess_pieces\WhiteKing.png', 'wk')
        
        self.bp1 = Pawn([self.get_place('bp1')[0],self.get_place('bp1')[1]],'black','Chess_pieces\BlackPawn.png', 'bp1')
        self.bp2 = Pawn([self.get_place('bp2')[0],self.get_place('bp2')[1]],'black','Chess_pieces\BlackPawn.png', 'bp2')
        self.bp3 = Pawn([self.get_place('bp3')[0],self.get_place('bp3')[1]],'black','Chess_pieces\BlackPawn.png', 'bp3')
        self.bp4 = Pawn([self.get_place('bp4')[0],self.get_place('bp4')[1]],'black','Chess_pieces\BlackPawn.png', 'bp4')
        self.bp5 = Pawn([self.get_place('bp5')[0],self.get_place('bp5')[1]],'black','Chess_pieces\BlackPawn.png', 'bp5')
        self.bp6 = Pawn([self.get_place('bp6')[0],self.get_place('bp6')[1]],'black','Chess_pieces\BlackPawn.png', 'bp6')
        self.bp7 = Pawn([self.get_place('bp7')[0],self.get_place('bp7')[1]],'black','Chess_pieces\BlackPawn.png', 'bp7')
        self.bp8 = Pawn([self.get_place('bp8')[0],self.get_place('bp8')[1]],'black','Chess_pieces\BlackPawn.png', 'bp8')
        
        self.wp1 = Pawn([self.get_place('wp1')[0],self.get_place('wp1')[1]],'white','Chess_pieces\whitePawn.png', 'wp1')
        self.wp2 = Pawn([self.get_place('wp2')[0],self.get_place('wp2')[1]],'white','Chess_pieces\whitePawn.png', 'wp2')
        self.wp3 = Pawn([self.get_place('wp3')[0],self.get_place('wp3')[1]],'white','Chess_pieces\whitePawn.png', 'wp3')
        self.wp4 = Pawn([self.get_place('wp4')[0],self.get_place('wp4')[1]],'white','Chess_pieces\whitePawn.png', 'wp4')
        self.wp5 = Pawn([self.get_place('wp5')[0],self.get_place('wp5')[1]],'white','Chess_pieces\whitePawn.png', 'wp5')
        self.wp6 = Pawn([self.get_place('wp6')[0],self.get_place('wp6')[1]],'white','Chess_pieces\whitePawn.png', 'wp6')
        self.wp7 = Pawn([self.get_place('wp7')[0],self.get_place('wp7')[1]],'white','Chess_pieces\whitePawn.png', 'wp7')
        self.wp8 = Pawn([self.get_place('wp8')[0],self.get_place('wp8')[1]],'white','Chess_pieces\whitePawn.png', 'wp8')
        
        self.pieces_list = [self.br1,self.br2,self.wr1,self.wr2,self.bb1,self.bb2,self.wb1,self.wb2,self.bn1,self.bn2,self.wn1,self.wn2,
                            self.bq,self.bk,self.wq,self.wk,self.bp1,self.bp2,self.bp3,self.bp4,self.bp5,self.bp6,self.bp7,self.bp8,
                            self.wp1,self.wp2,self.wp3,self.wp4,self.wp5,self.wp6,self.wp7,self.wp8]
    
    #This function is to make the board graphics
    def create_board(self):
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)
 
        rect_list = list() # this is the list of brown rectangle
 
        # used this loop to create a list of brown rectangles
        for i in range(0, 8): # control the row
            for j in range(0, 8): # control the column
                if i % 2 == 0: # which means it is an even row
                    if j % 2 != 0: # which means it is an odd column
                        rect_list.append(pygame.Rect(j * self.width, (i+1) * self.width, self.width, self.width))
                else:
                    if j % 2 == 0: # which means it is an even column
                        rect_list.append(pygame.Rect(j * self.width, (i+1) * self.width, self.width, self.width))
 
 
        # create main surface and fill the base color with light brown color
        self.chess_board_surface = pygame.Surface(self.size)
        self.chess_board_surface.fill(self.white)
 
        # next draws the dark brown rectangles on the chess board surface
        for chess_rect in rect_list:
            pygame.draw.rect(self.chess_board_surface, self.black, chess_rect)
        
        # draw black square
        pygame.draw.rect(self.chess_board_surface, (0,0,0), pygame.Rect(self.width*8,0,self.width*8+self.width*3,self.width*10))
        pygame.draw.rect(self.chess_board_surface, self.grey, pygame.Rect(0,0,self.width*8,self.width*1))
        pygame.draw.rect(self.chess_board_surface, self.grey, pygame.Rect(0,self.width*9,self.width*8,self.width*1))

        # draw the numbers and letters on board
        self.TextLN = myfont_board.render('1', 0, self.clear_white)
    
    #This function will be used to write +- points for each side and the moves played on the right
    def write_text(self):
        points_black = 0
        points_white = 0
        
        #Count the amount of points for each side
        for i in self.pieces_list:
            if(i.color == 'black' and i.position[0] != -1 and i.position[1] != -1):
                points_black += i.value
            elif(i.color == 'white' and i.position[0] != -1 and i.position[1] != -1):
                points_white += i.value        
          
        #Write the difference of points at the correct place
        if(self.top == 'black' and points_black > points_white):
            TextT = myfont_notation.render('Black  +' + str(points_black-points_white), 0,(0,0,0))
            TextB = myfont_notation.render('White',  0,self.clear_white)
        elif(self.top == 'black' and points_black == points_white):
            TextT = myfont_notation.render('Black',  0,(0,0,0))
            TextB = myfont_notation.render('White',  0,self.clear_white)
        elif(self.top == 'black' and points_black < points_white):
            TextT = myfont_notation.render('Black',  0,(0,0,0))
            TextB = myfont_notation.render('White  +' + str(points_white-points_black),  0,self.clear_white)
            
        if(self.top == 'white' and points_black < points_white):
            TextT = myfont_notation.render('White  +' + str(points_white-points_black),  0,self.clear_white)
            TextB = myfont_notation.render('Black',  0,(0,0,0))
        elif(self.top == 'white' and points_black == points_white):
            TextT = myfont_notation.render('White',  0,self.clear_white)
            TextB = myfont_notation.render('Black',  0,(0,0,0))
        elif(self.top == 'white' and points_black > points_white):
            TextT = myfont_notation.render('White',  0,self.clear_white)
            TextB = myfont_notation.render('Black  +' + str(points_black-points_white),  0,(0,0,0))
            
        #Update screen with new text
        self.screen.blit(TextT,(0,self.width*1-30))
        self.screen.blit(TextB,(0,self.width*9))
        
        #This is to write the moves played
        for i in range(1,9):                
             if(self.top == 'black'):
                 if(i%2 == 1):
                     self.TextN = myfont_board.render(str(i), 0, self.white)
                     self.TextL = myfont_board.render(chr(i+96), 0, self.white)
                    
                 else:
                     self.TextN = myfont_board.render(str(i), 0, self.black)
                     self.TextL = myfont_board.render(chr(i+96), 0, self.black)
                     
                 self.screen.blit(self.TextN,(0,self.width*(9-i)))
                
                 self.screen.blit(self.TextL,(self.width*(i)-10,self.width*9-22))
             else:
                 if(i%2 == 1):
                     self.TextN = myfont_board.render(str(i), 0, self.black)
                     self.TextL = myfont_board.render(chr(i+96), 0, self.black)
                    
                 else:
                     self.TextN = myfont_board.render(str(i), 0, self.white)
                     self.TextL = myfont_board.render(chr(i+96), 0, self.white)
                     
                 self.screen.blit(self.TextN,(0,self.width*(i)))

                 self.screen.blit(self.TextL,(self.width*(9-i)-10,self.width*9-22))               
    
    #Function to place the image of a piece in its position, uses the matrix of board to place the right piece
    def place_piece(self,x,y):
        
        name = self.get_piece(x, y)
        if(name != 'None'):
            img = pygame.image.load(getattr(self,name).image).convert_alpha()
            img = pygame.transform.scale(img, (self.width,self.width))
            self.chess_board_surface.blit(img, (x*self.width,(y+1)*self.width))
    
    #Loops through the whole board and calls the place piece function
    def add_pieces(self):
        # adding the pieces
        for i in range(len(self.board_pieces)):
            for j in range(len(self.board_pieces[i])):
                self.place_piece(i,j) 
    
    #Main movement function, it will go through all the pieces on the board and assign the possible moves them, also which pieces it protects
    #these moves are stored in an attribute of each pieces class, so it can be accessed anytime
    def all_movement(self,piece):
        piece.can_move.clear()
        piece.does_protect.clear()
        piece.move_not_eat.clear()
        
        #The logic for all pieces is the same, first get all the possible moves if the board was empty, then remove squares that are blocked
        #by other pieces, it will alos verify if the piece is 'pinned' meaning it protects the king from being eaten, if so then it can only move such that it
        #still protects the king.
        if (str(type(piece).__name__) == 'Knight'):
            x = piece.position[0]
            y = piece.position[1]
            
            if(x != -1 and y != -1):
                all_moves = [[x+2,y+1],[x+2,y-1],[x-2,y+1],[x-2,y-1],
                             [x+1,y+2],[x-1,y+2],[x+1,y-2],[x-1,y-2]]
                    
                for i in range(len(all_moves)):
                    if(all_moves[i][0] >= 0 and all_moves[i][0] <= 7 and all_moves[i][1] >= 0 and all_moves[i][1] <= 7):
                        pinned = self.is_pinned(piece)[0]
                        axis = self.is_pinned(piece)[1]
                        x_sign = geek.sign(all_moves[i][0] - piece.position[0])
                        y_sign = geek.sign(all_moves[i][1] - piece.position[1])
                        if(pinned == 'False'):
                            other_piece = self.get_piece(all_moves[i][0],all_moves[i][1])
                            if(self.king_check == piece.color):
                                if(self.block_check(all_moves[i][0], all_moves[i][1], piece.color) == True):
                                    piece.can_move.append(all_moves[i]) 
                            elif(other_piece == 'None'):
                                piece.can_move.append(all_moves[i])
                            elif(piece.color != getattr(self,other_piece).color):
                                piece.can_move.append(all_moves[i])
                            elif(piece.color == getattr(self,other_piece).color):
                                piece.does_protect.append(all_moves[i])
                            
        elif (str(type(piece).__name__) == 'Bishop'):
            x = piece.position[0]
            y = piece.position[1]
            if(x != -1 and y != -1):
                all_moves = [[]]
                all_moves.clear()
                for i in range(1,8):
                    all_moves.append([x+(1*i),y+(1*i)])
                    all_moves.append([x-(1*i),y-(1*i)])
                    all_moves.append([x+(1*i),y-(1*i)])
                    all_moves.append([x-(1*i),y+(1*i)])
                    
                for i in range(len(all_moves)):
                    if(all_moves[i][0] >= 0 and all_moves[i][0] <= 7 and all_moves[i][1] >= 0 and all_moves[i][1] <= 7):
                        if(self.piece_block(all_moves[i][0],all_moves[i][1],x,y) == True):
                            pinned = self.is_pinned(piece)[0]
                            axis = self.is_pinned(piece)[1]
                            x_sign = geek.sign(all_moves[i][0] - piece.position[0])
                            y_sign = geek.sign(all_moves[i][1] - piece.position[1])
                            if(pinned == 'False' or pinned == 'True' and axis == 'X' and all_moves[i][0] == piece.position[0] 
                               or pinned == 'True' and axis == 'Y' and all_moves[i][1] == piece.position[1] or pinned == 'True'
                               and axis == 'Same' and x_sign == y_sign or pinned == 'True' and axis == 'Dif' and x_sign != y_sign):
                                    other_piece = self.get_piece(all_moves[i][0],all_moves[i][1])
                                    if(self.king_check == piece.color):
                                        if(self.block_check(all_moves[i][0], all_moves[i][1], piece.color) == True):
                                            piece.can_move.append(all_moves[i]) 
                                    elif(other_piece == 'None'):
                                        piece.can_move.append(all_moves[i])
                                    elif(piece.color != getattr(self,other_piece).color):
                                        piece.can_move.append(all_moves[i])
                                    elif(piece.color == getattr(self,other_piece).color):
                                        piece.does_protect.append(all_moves[i])
                                    
        elif (str(type(piece).__name__) == 'Rook'):
            x = piece.position[0]
            y = piece.position[1]
            
            if(x != -1 and y != -1):            
                all_moves = [[]]
                all_moves.clear()
                for i in range(1,8):
                    all_moves.append([x+(1*i),y])
                    all_moves.append([x-(1*i),y])
                    all_moves.append([x,y-(1*i)])
                    all_moves.append([x,y+(1*i)])
                    
                for i in range(len(all_moves)):
                    if(all_moves[i][0] >= 0 and all_moves[i][0] <= 7 and all_moves[i][1] >= 0 and all_moves[i][1] <= 7):
                        if(self.piece_block(all_moves[i][0],all_moves[i][1],x,y) == True):
                            pinned = self.is_pinned(piece)[0]
                            axis = self.is_pinned(piece)[1]
                            x_sign = geek.sign(all_moves[i][0] - piece.position[0])
                            y_sign = geek.sign(all_moves[i][1] - piece.position[1])
                            if(pinned == 'False' or pinned == 'True' and axis == 'X' and all_moves[i][0] == piece.position[0] 
                               or pinned == 'True' and axis == 'Y' and all_moves[i][1] == piece.position[1] or pinned == 'True'
                               and axis == 'Same' and x_sign == y_sign and all_moves[i][0] != piece.position[0] and all_moves[i][1] != piece.position[1] 
                               or pinned == 'True' and axis == 'Dif' and x_sign != y_sign and all_moves[i][0] != piece.position[0] and all_moves[i][1] != piece.position[1]):
                                    other_piece = self.get_piece(all_moves[i][0],all_moves[i][1])
                                    if(self.king_check == piece.color):
                                        if(self.block_check(all_moves[i][0], all_moves[i][1], piece.color) == True):
                                            piece.can_move.append(all_moves[i]) 
                                    elif(other_piece == 'None'):
                                        piece.can_move.append(all_moves[i])
                                    elif(piece.color != getattr(self,other_piece).color):
                                        piece.can_move.append(all_moves[i])
                                    elif(piece.color == getattr(self,other_piece).color):
                                        piece.does_protect.append(all_moves[i])
                            
        elif (str(type(piece).__name__) == 'Queen'):
            x = piece.position[0]
            y = piece.position[1]
                    
            if(x != -1 and y != -1):
                all_moves = [[]]
                all_moves.clear()
                for i in range(1,8):
                    all_moves.append([x+(1*i),y])
                    all_moves.append([x-(1*i),y])
                    all_moves.append([x,y-(1*i)])
                    all_moves.append([x,y+(1*i)])
                    all_moves.append([x+(1*i),y+(1*i)])
                    all_moves.append([x-(1*i),y-(1*i)])
                    all_moves.append([x+(1*i),y-(1*i)])
                    all_moves.append([x-(1*i),y+(1*i)])
                    
                for i in range(len(all_moves)):
                    if(all_moves[i][0] >= 0 and all_moves[i][0] <= 7 and all_moves[i][1] >= 0 and all_moves[i][1] <= 7):
                        if(self.piece_block(all_moves[i][0],all_moves[i][1],x,y) == True):
                            pinned = self.is_pinned(piece)[0]
                            axis = self.is_pinned(piece)[1]
                            
                            x_sign = geek.sign(all_moves[i][0] - piece.position[0])
                            y_sign = geek.sign(all_moves[i][1] - piece.position[1])

                            if(pinned == 'False' or pinned == 'True' and axis == 'X' and all_moves[i][0] == piece.position[0] 
                               or pinned == 'True' and axis == 'Y' and all_moves[i][1] == piece.position[1] or pinned == 'True'
                               and axis == 'Same' and x_sign == y_sign and all_moves[i][0] != piece.position[0] and all_moves[i][1] != piece.position[1] 
                               or pinned == 'True' and axis == 'Dif' and x_sign != y_sign and all_moves[i][0] != piece.position[0] and all_moves[i][1] != piece.position[1]):
                                    other_piece = self.get_piece(all_moves[i][0],all_moves[i][1])
                                    if(self.king_check == piece.color):
                                        if(self.block_check(all_moves[i][0], all_moves[i][1], piece.color) == True):
                                            piece.can_move.append(all_moves[i]) 
                                    elif(other_piece == 'None'):
                                        piece.can_move.append(all_moves[i])
                                    elif(piece.color != getattr(self,other_piece).color):
                                        piece.can_move.append(all_moves[i])
                                    elif(piece.color == getattr(self,other_piece).color):
                                        piece.does_protect.append(all_moves[i])
                                
                        
        elif (str(type(piece).__name__) == 'King'):
            x = piece.position[0]
            y = piece.position[1]
                    
            all_moves = [[x+1,y],[x-1,y],[x,y+1],[x,y-1],
                         [x+1,y+1],[x+1,y-1],[x-1,y+1],[x-1,y-1]]
            
            if(self.castle(piece.color)[0] == 'L' and self.top == 'white'):
                all_moves.append([x+2,y])
            elif(self.castle(piece.color)[0] == 'L' and self.top == 'black'):
                all_moves.append([x-2,y])
            elif(self.castle(piece.color)[1] == 'S' and self.top == 'white'):
                all_moves.append([x-2,y])
            elif(self.castle(piece.color)[1] == 'S' and self.top == 'black'):
                all_moves.append([x+2,y])
                
            for i in range(len(all_moves)):
                if(all_moves[i][0] >= 0 and all_moves[i][0] <= 7 and all_moves[i][1] >= 0 and all_moves[i][1] <= 7):
                    #Replace this here by piece_protect
                    x_king = self.get_place('wk' if piece.name == 'bk' else 'bk')[0]
                    y_king = self.get_place('wk' if piece.name == 'bk' else 'bk')[1]
                    
                    if(abs(x_king - all_moves[i][0]) > 1 or abs(y_king - all_moves[i][1]) > 1):
                        if(self.piece_block(all_moves[i][0],all_moves[i][1],x,y) == True):
                            other_piece = self.get_piece(all_moves[i][0],all_moves[i][1])
                            if(other_piece == 'None') :
                                if(self.is_check(all_moves[i][0], all_moves[i][1], piece.color, True) == False):
                                    piece.can_move.append(all_moves[i])
                            else:
                                if(piece.color != getattr(self,other_piece).color):
                                    if(self.is_check(all_moves[i][0], all_moves[i][1], piece.color, False) == False):
                                        piece.can_move.append(all_moves[i])
                                else:
                                    piece.does_protect.append(all_moves[i])
                                    
        elif (str(type(piece).__name__) == 'Pawn'):
            x = piece.position[0]
            y = piece.position[1]
            if(x != -1 and y != -1):       
                all_moves = [[]]
                all_moves.clear()
                if(self.top != piece.color):
                    if((y-1) >= 0):
                        opp_name = self.get_piece(x, y-1)
                        if(opp_name == 'None'):
                            all_moves.append([x,y-1])
                    if(piece.position[1] == 6):
                        opp_name = self.get_piece(x, y-2)
                        if(opp_name == 'None'):
                            all_moves.append([x,y-2])
                    
                    if((x+1) <= 7 and (y-1) >= 0):
                        opp_name = self.get_piece(x+1, y-1)
                        if((opp_name != 'None' and getattr(self,opp_name).color != piece.color) or 
                           (self.en_passant != None and self.en_passant.position[1] == piece.position[1] and self.en_passant.position[0] == (piece.position[0] + 1))):
                            all_moves.append([x+1,y-1])
                        else:
                            piece.does_protect.append([x+1,y-1])
                    if((x-1) >= 0 and (y-1) >= 0):
                        opp_name = self.get_piece(x-1, y-1)
                        if((opp_name != 'None' and getattr(self,opp_name).color != piece.color) or 
                           (self.en_passant != None and self.en_passant.position[1] == piece.position[1] and self.en_passant.position[0] == (piece.position[0] - 1))):
                            all_moves.append([x-1,y-1])
                        else:
                            piece.does_protect.append([x-1,y-1])
                else:
                    if((y+1) <= 7):
                        opp_name = self.get_piece(x, y+1)
                        if(opp_name == 'None'):
                            all_moves.append([x,y+1])
                    if(piece.position[1] == 1):
                        opp_name = self.get_piece(x, y+2)
                        if(opp_name == 'None'):
                            all_moves.append([x,y+2])
                    
                    if((x+1) <= 7 and (y+1) <= 7):
                        opp_name = self.get_piece(x+1, y+1)
                        if((opp_name != 'None' and getattr(self,opp_name).color != piece.color) or 
                           (self.en_passant != None and self.en_passant.position[1] == piece.position[1] and self.en_passant.position[0] == (piece.position[0] + 1))):
                            all_moves.append([x+1,y+1])
                        else:
                            piece.does_protect.append([x+1,y+1])
                    if((x-1) >= 0 and (y+1) <= 7):
                        opp_name = self.get_piece(x-1, y+1)
                        if((opp_name != 'None' and getattr(self,opp_name).color != piece.color) or 
                           (self.en_passant != None and self.en_passant.position[1] == piece.position[1] and self.en_passant.position[0] == (piece.position[0] + 1))):
                            all_moves.append([x-1,y+1])
                        else:
                            piece.does_protect.append([x-1,y+1])
                    
                for i in range(len(all_moves)):
                    if(all_moves[i][0] >= 0 and all_moves[i][0] <= 7 and all_moves[i][1] >= 0 and all_moves[i][1] <= 7):
                        #Replace this here by piece_protect
                        if(self.piece_block(all_moves[i][0],all_moves[i][1],x,y) == True):
                            pinned = self.is_pinned(piece)[0]
                            axis = self.is_pinned(piece)[1]
                            x_sign = geek.sign(all_moves[i][0] - piece.position[0])
                            y_sign = geek.sign(all_moves[i][1] - piece.position[1])
                            if(pinned == 'False' or pinned == 'True' and axis == 'X' and all_moves[i][0] == piece.position[0] 
                               or pinned == 'True' and axis == 'Y' and all_moves[i][1] == piece.position[1] or pinned == 'True'
                               and axis == 'Same' and x_sign == y_sign and all_moves[i][0] != piece.position[0] and all_moves[i][1] != piece.position[1] 
                               or pinned == 'True' and axis == 'Dif' and x_sign != y_sign and all_moves[i][0] != piece.position[0] and all_moves[i][1] != piece.position[1]):
                                    other_piece = self.get_piece(all_moves[i][0],all_moves[i][1])
                                    if(self.king_check == piece.color):
                                        if(self.block_check(all_moves[i][0], all_moves[i][1], piece.color) == True):
                                            if(piece.position[0] == all_moves[i][0]):
                                                piece.move_not_eat.append(all_moves[i])
                                            else:    
                                                piece.can_move.append(all_moves[i]) 
                                    elif(other_piece == 'None'):
                                        if(piece.position[0] == all_moves[i][0]):
                                            piece.move_not_eat.append(all_moves[i])
                                        else:    
                                            piece.can_move.append(all_moves[i])
                                    elif(piece.color != getattr(self,other_piece).color):
                                        if(piece.position[0] == all_moves[i][0]):
                                            piece.move_not_eat.append(all_moves[i])
                                        else:    
                                            piece.can_move.append(all_moves[i])
    
    #function to loop through all the pieces and call the previous function to get their possible moves
    def populate_moves(self):
        for i in self.pieces_list:
            if(i.color != self.get_color_turn()):
                self.all_movement(i)
        for i in self.pieces_list:
            if(i.color == self.get_color_turn()):
                self.all_movement(i)
    
    #Will highlight the possible moves of the selected piece on the board, will also remove the previously selected piece possible moves
    def highlight_movement(self):
        if(self.previously_selected != None):
            for i in self.previously_selected.can_move + self.previously_selected.move_not_eat:
                self.color(i[0],i[1])
        if(self.click[0] != -1 and self.click[1] != -1):
            for i in self.selected_piece.can_move + self.selected_piece.move_not_eat:
                self.color_move(i[0],i[1])        
    
    #Simply returns the piece at a certain coordinate
    def get_piece(self,x,y):
        return str(self.board_pieces[x][y])
    
    #Returns the coordinate of a certain piece
    def get_place(self,name):
        for i in range(len(self.board_pieces)):
            for j in range(len(self.board_pieces[i])):
                if self.board_pieces[i][j] == name:
                    return (i, j)
                
    #Get the color of the player's turn to play
    def get_color_turn(self):
        if(self.turn % 2 == 1):
            return self.start
        else:
            return self.second
    
    #Function used in all_movement to see if the square x_move,y_move is blocked by a piece from square x,y
    def piece_block(self,x_move,y_move,x,y):
        if(x_move == x):
            for i in range(1,abs(y_move - y)):
                if((y_move - y) < 0):
                    if(self.get_piece(x_move,y_move + i) != 'None'):
                        return False
                else:
                    if(self.get_piece(x_move,y_move - i) != 'None'):
                        return False
        elif(y_move == y):
            for i in range(1,abs(x_move - x)):
                if((x_move - x) < 0):
                    if(self.get_piece(x_move + i,y_move) != 'None'):
                        return False
                else:
                    if(self.get_piece(x_move - i,y_move) != 'None'):
                        return False
        else:
            for i in range(1,abs(x_move - x)):
                if(((x_move - x) < 0) and ((y_move - y) < 0)):
                    if(self.get_piece(x_move + i,y_move + i) != 'None'):
                        return False
                elif(((x_move - x) > 0) and ((y_move - y) < 0)):
                    if(self.get_piece(x_move - i,y_move + i) != 'None'):
                        return False
                elif(((x_move - x) < 0) and ((y_move - y) > 0)):
                    if(self.get_piece(x_move + i,y_move - i) != 'None'):
                        return False
                elif(((x_move - x) > 0) and ((y_move - y) > 0)):
                    if(self.get_piece(x_move - i,y_move - i) != 'None'):
                        return False
        return True
        
    #This is also used in all_movement to see if a piece is pinned to king, and if so will return on which axis it can move and still protect the king
    def is_pinned(self,piece):
        if(piece.color == self.get_color_turn()):
            x_king = self.get_place('bk' if self.get_color_turn() == 'black' else 'wk')[0]
            y_king = self.get_place('bk' if self.get_color_turn() == 'black' else 'wk')[1]
            
            square_between = self.get_points_between(x_king, y_king, piece.position[0], piece.position[1])
            
            if(len(square_between) > 0):
                for i in range(len(square_between)):
                    name = self.get_piece(square_between[i][0], square_between[i][1])
                    if(name != 'None'):
                        return 'False', 'N'
            
            if(piece.position[0] == x_king):
                for i in self.pieces_list:
                    for j in range(len(i.can_move)):
                        if(i.can_move[j][0] == piece.position[0] and i.can_move[j][1] == piece.position[1] and i.position[0] == piece.position[0] and i.color != piece.color):
                            return 'True', 'X'
                return 'False', 'N'
                    
            elif(piece.position[1] == y_king):
                for i in self.pieces_list:
                    for j in range(len(i.can_move)):
                        if(i.can_move[j][0] == piece.position[0] and i.can_move[j][1] == piece.position[1] and i.position[1] == piece.position[1] and i.color != piece.color):
                            return 'True', 'Y'
                return 'False', 'N'
            
            else:
                for i in self.pieces_list:
                    if fnmatch.fnmatch(i.name, '?[!p]*'):
                        for j in range(len(i.can_move)):
                            x_sign = geek.sign(piece.position[0] - x_king)
                            y_sign = geek.sign(piece.position[1] - y_king)

                            if(i.can_move[j][0] == piece.position[0] and i.can_move[j][1] == piece.position[1] and i.position[1] != piece.position[1] and i.position[0] != piece.position[0] 
                               and i.color != piece.color and x_sign == y_sign and abs(i.position[0] - x_king) == abs(i.position[1] - y_king)):
                                return 'True', 'Same'
                            elif(i.can_move[j][0] == piece.position[0] and i.can_move[j][1] == piece.position[1] and i.position[1] != piece.position[1] and i.position[0] != piece.position[0] 
                                 and i.color != piece.color and x_sign != y_sign and abs(i.position[0] - x_king) == abs(i.position[1] - y_king)):
                                return 'True', 'Dif'               
        return 'False', 'N'
    
    #To put correct color on square x,y
    def color(self,x,y):
        if x % 2 == 0: # which means it is an even row
                  if y % 2 != 0: # which means it is an odd column
                      pygame.draw.rect(self.chess_board_surface, self.black, pygame.Rect((x) * self.width, (y+1) * self.width, self.width, self.width))
                      self.place_piece(x,y)
                  else:
                      pygame.draw.rect(self.chess_board_surface, self.white, pygame.Rect((x) * self.width, (y+1) * self.width, self.width, self.width))
                      self.place_piece(x,y)
        else:
                  if y % 2 == 0: # which means it is an even column
                      pygame.draw.rect(self.chess_board_surface, self.black, pygame.Rect((x) * self.width, (y+1) * self.width, self.width, self.width))
                      self.place_piece(x,y)
                  else:
                      pygame.draw.rect(self.chess_board_surface, self.white, pygame.Rect((x) * self.width, (y+1) * self.width, self.width, self.width))
                      self.place_piece(x,y)
      
    #Will highlight the square x,y, it will also run the function highilght_check to highlight if a there is a check
    def highlight_square(self,x,y):
        self.original_color = self.chess_board_surface.get_at((x * self.width + 10, (y+1) * self.width + 10))

        if self.original_color.r == self.highlight[0] and self.original_color.g == self.highlight[1] and self.original_color.b == self.highlight[2]:
            self.color(x,y)
            self.click[0] = -1
            self.click[1] = -1
            
        else:
            pygame.draw.rect(self.chess_board_surface, self.highlight, pygame.Rect((x) * self.width, (y+1) * self.width, self.width, self.width))
            self.place_piece(x,y)
            if self.click[0] >= 0 and self.click[1] >= 0:
                if self.click[0] % 2 == 0: # which means it is an even row
                  if self.click[1] % 2 != 0: # which means it is an odd column
                      pygame.draw.rect(self.chess_board_surface, self.black, pygame.Rect((self.click[0]) * self.width, (self.click[1]+1) * self.width, self.width, self.width))
                      self.place_piece(self.click[0],self.click[1])
                  else:
                      pygame.draw.rect(self.chess_board_surface, self.white, pygame.Rect((self.click[0]) * self.width, (self.click[1]+1) * self.width, self.width, self.width))
                      self.place_piece(self.click[0],self.click[1])
                else:
                  if self.click[1] % 2 == 0: # which means it is an even column
                      pygame.draw.rect(self.chess_board_surface, self.black, pygame.Rect((self.click[0]) * self.width, (self.click[1]+1) * self.width, self.width, self.width))
                      self.place_piece(self.click[0],self.click[1])
                  else:
                      pygame.draw.rect(self.chess_board_surface, self.white, pygame.Rect((self.click[0]) * self.width, (self.click[1]+1) * self.width, self.width, self.width))
                      self.place_piece(self.click[0],self.click[1])
            self.click[0] = x
            self.click[1] = y
            
        self.highlight_check()
    
    #The previous move will stay in a gray square 
    def color_move(self,x,y):
        outline_width = 4
        pygame.draw.rect(self.chess_board_surface, self.move_color, pygame.Rect((x) * self.width, (y+1) * self.width, self.width, outline_width))
        pygame.draw.rect(self.chess_board_surface, self.move_color, pygame.Rect((x) * self.width, (y+1) * self.width, outline_width, self.width))
        pygame.draw.rect(self.chess_board_surface, self.move_color, pygame.Rect((x) * self.width, ((y + 2) * self.width) - outline_width, self.width, outline_width))
        pygame.draw.rect(self.chess_board_surface, self.move_color, pygame.Rect(((x + 1) * self.width) - outline_width, (y+1) * self.width, outline_width, self.width))
    
    #Will verify if king of a certain color is in check 
    def is_check(self,x,y,color,king):
        for i in self.pieces_list:
            if(i.color != color):
                for j in i.can_move + i.does_protect:
                    if(j[0] == x and j[1] == y):
                        return True
                     
                    if(king == True and self.king_check == color):
                        if(color == 'black'):
                            if(j[0] == self.get_place('bk')[0] and j[1] == self.get_place('bk')[1]):
                                if(i.position[0] == x and j[0] == x):
                                    return True
                                if(i.position[1] == y and j[1] == y):
                                    return True
                                if(abs(i.position[0] - x) == abs(i.position[1] - y) and geek.sign(i.position[0] - x) == geek.sign(j[0] - x)
                                    and geek.sign(i.position[1] - y) == geek.sign(j[1] - y)):
                                    return True
                        else:
                            if(j[0] == self.get_place('wk')[0] and j[1] == self.get_place('wk')[1]):
                                if(i.position[0] == x and j[0] == x):
                                    return True
                                if(i.position[1] == y and j[1] == y):
                                    return True
                                if(abs(i.position[0] - x) == abs(i.position[1] - y) and geek.sign(i.position[0] - x) == geek.sign(j[0] - x)
                                    and geek.sign(i.position[1] - y) == geek.sign(j[1] - y)):
                                    return True
        return False 
    
    #Function to see if the game is over, can be stalemate, or checkmate
    def is_done(self):
        if(self.king_check != None):
            for i in self.pieces_list:
                if(i.color == self.king_check and (len(i.can_move) != 0 or len(i.move_not_eat) != 0)):
                    return False
            return 'check'
        elif(self.king_check == None):
            for i in self.pieces_list:
                if(i.color == self.get_color_turn() and (len(i.can_move) != 0 or len(i.move_not_eat) != 0)):
                    return False
            self.result = '1/2-1/2'
            self.textgame_string += ' ' + self.result
            return 'stale'         
        return False
    
    #This is used in all_movement to see if a certain move blocks check, if it does then it can be played when the player is in check                
    def block_check(self,x,y,color):
        piece_check = None
        nbr_piece_check = 0
        
        if(color == 'black'):
            x_king = self.bk.position[0]
            y_king = self.bk.position[1]
        else:
            x_king = self.wk.position[0]
            y_king = self.wk.position[1]
            
        for i in self.pieces_list:
            if(i.color != color):
                for j in i.can_move:
                    if(j[0] == x_king and j[1] == y_king):
                        if(nbr_piece_check == 0):
                            piece_check = i
                        nbr_piece_check += 1
        
        if(nbr_piece_check >= 2):
            return False
        elif(nbr_piece_check == 1):
            if(x == piece_check.position[0] and y == piece_check.position[1]):
                return True
            if(str(type(piece_check).__name__) == 'Knight'):
                return False
            points = self.get_points_between(x_king,y_king,piece_check.position[0],piece_check.position[1])
            for i in range(len(points)):
                if(x == points[i][0] and y == points[i][1]):
                    return True
            return False
        return True        
    
    #Triangulation function used to see if a player is in check, return the coordinates of squares between two pieces
    def get_points_between(self,x,y,other_x,other_y):
            points = [[]]
            points.clear()
            
            if(x == other_x):
                if(y > other_y):
                    for i in range(other_y + 1,y):
                        points.append([x,i])
                else:
                    for i in range(y + 1,other_y):
                        points.append([x,i])
                return points
            
            if(y == other_y):
                if(x > other_x):
                    for i in range(other_x + 1,x):
                        points.append([i,y])
                else:
                    for i in range(x + 1,other_x):
                        points.append([i,y])
                return points
            
            for i in range(1,abs(other_x - x)):
                    if(((other_x - x) < 0) and ((other_y - y) < 0) and abs(other_x-x) == abs(other_y-y)):
                        points.append([x-i,y-i])
                    elif(((other_x  - x) > 0) and ((other_y - y) < 0) and abs(other_x-x) == abs(other_y-y)):
                        points.append([x+i,y-i])
                    elif(((other_x  - x) < 0) and ((other_y - y) > 0) and abs(other_x-x) == abs(other_y-y)):
                        points.append([x-i,y+i])
                    elif(((other_x  - x) > 0) and ((other_y - y) > 0) and abs(other_x-x) == abs(other_y-y)):
                        points.append([x+i,y+i])
            return points    
    
    #Function to highlight in red the king which is in check
    def highlight_check(self):
        if(self.king_check == None):
            if(self.get_color_turn() == 'black'):
                self.color(self.wk.position[0],self.wk.position[1])
                self.place_piece(self.wk.position[0],self.wk.position[1])
            else:
                self.place_piece(self.bk.position[0], self.bk.position[1])
                self.color(self.bk.position[0],self.bk.position[1])
                
        elif(self.king_check == 'black'):
            x = self.bk.position[0]
            y = self.bk.position[1]
            outline_width = 4
            pygame.draw.rect(self.chess_board_surface, self.red, pygame.Rect((x) * self.width, (y+1) * self.width, self.width, outline_width))
            pygame.draw.rect(self.chess_board_surface, self.red, pygame.Rect((x) * self.width, (y+1) * self.width, outline_width, self.width))
            pygame.draw.rect(self.chess_board_surface, self.red, pygame.Rect((x) * self.width, ((y + 2) * self.width) - outline_width, self.width, outline_width))
            pygame.draw.rect(self.chess_board_surface, self.red, pygame.Rect(((x + 1) * self.width) - outline_width, (y+1) * self.width, outline_width, self.width))
        elif(self.king_check == 'white'):
            x = self.wk.position[0]
            y = self.wk.position[1]
            outline_width = 4
            pygame.draw.rect(self.chess_board_surface, self.red, pygame.Rect((x) * self.width, (y+1) * self.width, self.width, outline_width))
            pygame.draw.rect(self.chess_board_surface, self.red, pygame.Rect((x) * self.width, (y+1) * self.width, outline_width, self.width))
            pygame.draw.rect(self.chess_board_surface, self.red, pygame.Rect((x) * self.width, ((y + 2) * self.width) - outline_width, self.width, outline_width))
            pygame.draw.rect(self.chess_board_surface, self.red, pygame.Rect(((x + 1) * self.width) - outline_width, (y+1) * self.width, outline_width, self.width))
    
    #Function make the piece move. First it will make sure it is a legal move, then it will see if it is a capture, if yes then it will remove the old piece and add the new one
    #All this has to be done on the screen as well as in the matrix keeping track of the board
    def move_piece(self,x,y):
        castle = False
        take = False
        promote = False
        
        if(len(self.selected_piece.can_move) != 0 or len(self.selected_piece.move_not_eat) != 0):
            old_x = self.selected_piece.position[0]
            old_y = self.selected_piece.position[1]
            name = self.get_piece(old_x, old_y)
            #Check if legal move by looping through all possible moves
            for i in self.selected_piece.can_move + self.selected_piece.move_not_eat:
                if(x == i[0] and y == i[1]):
                    #If yes then insert its new coordinates
                    self.selected_piece.position.clear()
                    self.selected_piece.position = [x,y]
                    name_opp = self.get_piece(x, y)
                    
                    #Verifying for en passant
                    if(str(type(self.selected_piece).__name__) == 'Pawn' and x != old_x and name_opp == 'None'):
                        name_opp = self.en_passant.name
                        self.board_pieces[self.en_passant.position[0]][self.en_passant.position[1]] = 'None'
                        self.color(self.en_passant.position[0],self.en_passant.position[1])
                    
                    #If eating another piece then make sure to remove it
                    if(name_opp != 'None'):
                        take = True
                        getattr(self,name_opp).position.clear()
                        getattr(self,name_opp).position = [-1,-1]
                        getattr(self,name_opp).can_move.clear()
                        getattr(self,name_opp).move_not_eat.clear()
                    self.board_pieces[x][y] = name
                    self.board_pieces[old_x][old_y] = 'None'
                    for j in self.selected_piece.can_move + self.selected_piece.move_not_eat:
                        self.color(j[0],j[1])
                    self.place_piece(x, y)
                    self.color(old_x,old_y)
                    promote = self.promote(x,y,self.selected_piece.color)
                    
                    if(str(type(self.selected_piece).__name__) == 'Pawn' and abs(old_y - y) == 2):
                        self.en_passant = self.selected_piece
                    else:
                        self.en_passant = None
                    
                    #Verify if castling if it is a king move
                    if((name == 'wk' or name == 'bk') and abs(old_x-x) > 1):
                        if(old_x-x > 0):
                            if(self.top == 'white'):
                                castle = 'S'
                            else:
                                castle = 'L'
                            name_rook = self.get_piece(0, y)
                            self.board_pieces[0][y] = 'None'
                            self.board_pieces[old_x-1][y] = name_rook
                            getattr(self,name_rook).position.clear
                            getattr(self,name_rook).position = [old_x-1,y]
                            self.color(0,y)
                            self.place_piece(old_x-1, y)
                        else:
                            if(self.top == 'white'):
                                castle = 'L'
                            else:
                                castle = 'S'
                            name_rook = self.get_piece(7, y)
                            self.board_pieces[7][y] = 'None'
                            self.board_pieces[old_x+1][y] = name_rook
                            getattr(self,name_rook).position.clear
                            getattr(self,name_rook).position = [old_x+1,y]
                            self.color(7,y)
                            self.place_piece(old_x+1, y)
                    
                    #Recalculate the possible moves for all pieces as the board has changed
                    self.populate_moves()
                    if(self.get_color_turn() == 'white' and self.is_check(self.bk.position[0], self.bk.position[1], 'black', False)):
                        self.king_check = 'black'
                    elif(self.get_color_turn() == 'black' and self.is_check(self.wk.position[0], self.wk.position[1], 'white', False)):
                        self.king_check = 'white'
                    else:
                        self.king_check = None
                    
                    #If it is a king or rook move then we remove the right to castle on that side
                    self.selected_piece = None
                    if(name == 'wk'): self.can_castle_long_w, self.can_castle_short_w = False, False
                    elif(name == 'bk'): self.can_castle_long_b, self.can_castle_short_b = False, False
                    elif(self.top == 'black'):
                        if(name == 'br1'): self.can_castle_long_b = False
                        elif(name == 'br2'): self.can_castle_short_b = False
                        elif(name == 'wr1'): self.can_castle_short_w = False
                        elif(name == 'wr2'): self.can_castle_long_w = False
                    elif(self.top == 'white'):
                        if(name == 'br1'): self.can_castle_short_b = False
                        elif(name == 'br2'): self.can_castle_long_b = False
                        elif(name == 'wr1'): self.can_castle_long_w = False
                        elif(name == 'wr2'): self.can_castle_short_w = False
                        
                    self.notation(x,y,name,take,castle,promote, old_x, old_y)
                    self.turn += 1
                    return True
        return False
    
    #Function to take into account if a pawn has reached the end of the board, it will promote automatically to a new queen.
    #So delete the pawn a and create a new queen
    def promote(self,x,y,color):
        
        namepawn = self.get_piece(x, y)
        if fnmatch.fnmatch(namepawn, '?p?'):
            if(color != self.top and y == 0):
                if(color == 'black'):
                    self.nbr_queens_b += 1
                    name = 'bq' + str(self.nbr_queens_b)
                    setattr(self,name,Queen(self.width*[x,y],'black','BlackQueen.png', name))
                if(color == 'white'):
                    self.nbr_queens_w += 1
                    name = 'wq' + str(self.nbr_queens_w)
                    setattr(self,name,Queen(self.width*[x,y],'white','WhiteQueen.png',name))
                self.board_pieces[x][y] = name
                self.pieces_list.append(getattr(self,name))
                self.color(x, y)
                self.place_piece(x, y)
                getattr(self,namepawn).position.clear()
                getattr(self,namepawn).position = [-1,-1]
                getattr(self,namepawn).can_move.clear()
                getattr(self,namepawn).move_not_eat.clear()
                
                return True
            elif(color == self.top and y == 7):
                if(color == 'black'):
                    self.nbr_queens_b += 1
                    name = 'bq' + str(self.nbr_queens_b)
                    setattr(self,name,Queen(self.width*[x,y],'black','BlackQueen.png', name))
                if(color == 'white'):
                    self.nbr_queens_w += 1
                    name = 'wq' + str(self.nbr_queens_w)
                    setattr(self,name,Queen(self.width*[x,y],'white','WhiteQueen.png', name))
                self.board_pieces[x][y] = name
                self.pieces_list.append(getattr(self,name))
                self.color(x, y)
                self.place_piece(x, y)
                getattr(self,namepawn).position.clear()
                getattr(self,namepawn).position = [-1,-1]
                getattr(self,namepawn).can_move.clear()
                getattr(self,namepawn).move_not_eat.clear()      
                
                return True
        return False
    
    #Function to return if a king of a certain color can castle long, short or both, by looking at movement indicator that is modified in the move piece function
    def castle(self, color):
        value = ['N','N']
        if(color == self.get_color_turn()):
            if(color == 'white'):
                if(self.can_castle_long_w == True):
                    if(self.top == 'white'):
                        if(self.get_piece(6,0) == 'None' and self.get_piece(5, 0) == 'None' and self.get_piece(4, 0) == 'None'
                            and self.is_check(4,0,color,False) == False and self.is_check(5,0,color,False) == False and self.king_check != color):
                            value[0] = 'L'
                    elif(self.top == 'black'):
                        if(self.get_piece(1,7) == 'None' and self.get_piece(2, 7) == 'None' and self.get_piece(3, 7) == 'None'
                            and self.is_check(3,7,color,False) == False and self.is_check(2,7,color,False) == False and self.king_check != color):
                            value[0] = 'L'
                if(self.can_castle_short_w == True):
                    if(self.top == 'white'):
                        if(self.get_piece(1,0) == 'None' and self.get_piece(2, 0) == 'None'
                            and self.is_check(1,0,color,False) == False and self.is_check(2,0,color,False) == False and self.king_check != color):
                            value[1] = 'S'
                    elif(self.top == 'black'):
                        if(self.get_piece(6,7) == 'None' and self.get_piece(5, 7) == 'None'
                            and self.is_check(6,7,color,False) == False and self.is_check(5,7,color,False) == False and self.king_check != color):
                            value[1] = 'S'
            
            elif(color == 'black'):
                if(self.can_castle_long_b == True):
                    if(self.top == 'white'):
                        if(self.get_piece(6,7) == 'None' and self.get_piece(5, 7) == 'None' and self.get_piece(4, 7) == 'None'
                            and self.is_check(5,7,color,False) == False and self.is_check(4,7,color,False) == False and self.king_check != color):
                            value[0] = 'L'
                    if(self.top == 'black'):
                        if(self.get_piece(1,0) == 'None' and self.get_piece(2, 0) == 'None' and self.get_piece(3, 0) == 'None'
                            and self.is_check(3,0,color,False) == False and self.is_check(2,0,color,False) == False and self.king_check != color):
                            value[0] = 'L'
                if(self.can_castle_short_b == True):
                    if(self.top == 'white'):
                        if(self.get_piece(1,7) == 'None' and self.get_piece(2, 7) == 'None'
                            and self.is_check(1,7,color,False) == False and self.is_check(2,7,color,False) == False and self.king_check != color):
                            value[1] = 'S'
                    if(self.top == 'black'):
                        if(self.get_piece(6,0) == 'None' and self.get_piece(5, 0) == 'None'
                            and self.is_check(6,0,color,False) == False and self.is_check(5,0,color,False) == False and self.king_check != color):
                            value[1] = 'S'
        return value
    
    #To render text    
    def blitlines(self, surf, text, renderer, color, x, y):
        pygame.draw.rect(self.chess_board_surface, (0,0,0), pygame.Rect(self.width*8,0,self.width*8+self.width*3,self.width*8))
        height = renderer.get_height()
        lines = text.split('\n')
        for i, j in enumerate(lines):
            txt_surface = renderer.render(j, True, color)
            surf.blit(txt_surface, (x, y+(i*height)))
    
    #Writes the strings for the move notation that is printed on the screen
    def notation(self, x, y, name, take, castle, promote, orig_x, orig_y):
        verify = False
        nbr_chr = 0
        
        if(self.turn % 2 == 1):
            self.textgame_string += (str(self.turn // 2 + self.turn % 2) + '. ')
            if((self.turn // 2 + self.turn % 2) < 10):
                self.textgame_string += ('  ')
            
        if(castle == 'S'):
            self.textgame_string += ('0-0')
            nbr_chr = 4
        elif(castle == 'L'):
            self.textgame_string += ('0-0-0')
            nbr_chr = 6
        else:    
            if fnmatch.fnmatch(name, '?r?'):
                self.textgame_string += ('R')
                verify = True
                nbr_chr += 3
            elif  fnmatch.fnmatch(name, '?b?'):
                self.textgame_string += ('B')
                nbr_chr += 3
            elif  fnmatch.fnmatch(name, '?p?'):
                if(take == True):
                    if(self.top == 'black'):
                        self.textgame_string += (chr(orig_x+97))
                        nbr_chr += 1
                    else:
                        self.textgame_string += (chr(104-orig_x))
                        nbr_chr += 1
            elif  fnmatch.fnmatch(name, '?n?'):
                self.textgame_string += ('N')
                verify = True
                nbr_chr += 3
            elif  fnmatch.fnmatch(name, '?k'):
                self.textgame_string += ('K')
                nbr_chr += 3
            elif  fnmatch.fnmatch(name, '?q*'):
                self.textgame_string += ('Q')
                verify = True
                nbr_chr += 3
            
            if(verify == True):
                for i in self.pieces_list:
                    if(i.name[0:2] == name[0:2] and i.name != name):                       
                        for j in i.does_protect:
                                if(j[0] == x and j[1] == y):
                                    if(i.position[0] == orig_x):
                                        if(self.top == 'black'):
                                            self.textgame_string += (str(8-orig_y))
                                            nbr_chr += 1
                                        else:
                                            self.textgame_string += (str(orig_y+1))
                                            nbr_chr += 1
                                    else:
                                        if(self.top == 'black'):
                                            self.textgame_string += (chr(orig_x+97))
                                            nbr_chr += 1
                                        else:
                                            self.textgame_string += (chr(104-orig_x))
                                            nbr_chr += 1
                                    
            if(take == True):
                self.textgame_string += ('x')
                nbr_chr += 3
            
            if(self.top == 'black'):
                self.textgame_string += (chr(x+97))
                nbr_chr += 1
            else:
                self.textgame_string += (chr(104-x))
                nbr_chr += 1
            
            if(self.top == 'black'):
                self.textgame_string += (str(8-y))
                nbr_chr += 1
            else:
                self.textgame_string += (str(y+1))
                nbr_chr += 1
            
            if(promote == True):
                self.textgame_string += ('=Q')
                nbr_chr += 3
            
            self.populate_moves()
            if(self.is_done() == 'check'):
                self.textgame_string += ('#')
                if(self.king_check == 'black'):
                    self.result = '1-0'
                    self.textgame_string += ' ' + self.result
                else:
                    self.result = '0-1'
                    self.textgame_string += ' ' + self.result
            elif(self.king_check != self.get_color_turn() and self.king_check != None):
                self.textgame_string += ('+')
                nbr_chr += 1
            
        for i in range(15 - nbr_chr):
            self.textgame_string += (' ')
            
            
        if(self.turn % 2 != 1):
            self.textgame_string += ('\n')    
    
    #Transforms the text of moves to a .txt file that can be uploaded into a chess website or engine to be analyzed 
    def create_pgn(self):
        self.text_pgn = '[Event "?"]\n[Site "?"]\n[Round "1"]\n[White "White"]\n[Black "Black"]\n[Result "' + self.result + '"]\n \n'
        
        self.text_pgn += self.textgame_string.replace('\n', ' ')
        
        counter = 0
        spaces = 0
        for i in self.text_pgn:
            if(i == ' ' and spaces == 1):
                self.text_pgn = self.text_pgn[:counter-1] + self.text_pgn[counter:]
            elif(i == ' '):
                spaces = 1
                counter += 1
            else:
                spaces = 0
                counter += 1
                
        with open("ChessGame1.pgn", "w") as file:
            file.write(self.text_pgn)
    
    #Function that puts it all together to play
    def play(self):
        while True:
            for event in pygame.event.get():
                did_move = False
                if event.type == pygame.QUIT: 
                    pygame.display.quit()
                    sys.exit(0)
                #Get the x,y coordinate that the mouse clicked on
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    x = math.floor(pos[0] / self.width)
                    y = math.floor(pos[1] / self.width) - 1
                    #If it is in the right black square then print the pgn
                    if(x > 7 or y < 0 or y > 7):
                        self.create_pgn()
                        print(self.text_pgn)
                        
                    else:
                        #Verify a good color piece is selected and then highlight moves
                        self.populate_moves()
                        
                        if(self.selected_piece != None):
                            did_move = self.move_piece(x, y)
                        
                        if(did_move == False):
                            name = self.get_piece(x, y)
                            if(name != 'None'):
                                if(self.selected_piece != None and getattr(self,name).color  == self.get_color_turn()):
                                    self.previously_selected = self.selected_piece
                                if(getattr(self,name).color  == self.get_color_turn()):
                                    self.selected_piece = getattr(self,name)    

                        self.highlight_check()
                        self.populate_moves()
                        if(name != 'None' and getattr(self,name).color == self.get_color_turn() and did_move == False):
                                self.highlight_square(x, y)
                                self.highlight_movement()
                        
                        self.blitlines(self.chess_board_surface, self.textgame_string, myfont_notation, self.clear_white, self.width*8, 0)
                        
                        #Check if the game is done else keep looping 
                        if(self.is_done() == 'check' or self.is_done() == 'stale'):
                            self.screen.blit(self.chess_board_surface, (0, 0))
                            pygame.display.update()
                            if(self.is_done() == 'check'):
                                textsurface = myfont.render('Checkmate !', 0, self.red)
                            elif(self.is_done() == 'stale'):
                                textsurface = myfont.render('Stalemate !', 0, self.red)
                            self.screen.blit(textsurface,(self.width*2,self.width*4))
                            self.write_text()
                            pygame.display.update()
                            while True:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT: 
                                        pygame.display.quit()
                                        sys.exit(0)
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        pos = event.pos
                                        x = math.floor(pos[0] / self.width)
                                        y = math.floor(pos[1] / self.width) - 1
                                        if(x > 7 or y < 0 or y > 7):
                                            self.create_pgn()
                                            print(self.text_pgn)
                                        else:    
                                            pygame.display.quit()
                                            sys.exit(0)
                                         
                # displayed the chess surface
                self.screen.blit(self.chess_board_surface, (0, 0))
                self.write_text()
                pygame.display.update()
    
    

        