
import numpy as np
from  .disc import Disc
WIDTH = 7
HEIGHT = 6
PLAYER1= 1
PLAYER2= 2


class Board:
    def __init__(self):
        self.__width = WIDTH
        self.__height = HEIGHT
        self.__discs = []
        self.__list_board = self.cell_list()

    def __str__(self):
        board = np.zeros((HEIGHT, WIDTH))
        for row in range(HEIGHT):
            for col in range(WIDTH):
                if self.__list_board[row][col] is not None:
                    board[row][col] = self.__list_board[row][col]
        return str(board)

    def cell_list(self):
        """
        :return: list of all the coordinates of the board
        """
        board_list = []
        for row in range(self.__height):
            board_list.append([])
            for col in range(self.__width):
                board_list[row].append(None)
        return board_list

    def board_is_full(self):
        if len(self.__discs) == WIDTH*HEIGHT:
            return True
        return False



    def get_list_board(self):
        """return the board list"""
        return self.__list_board

    def get_width(self):
        """return the board width"""
        return self.__width

    def get_height(self):
        """return the board height"""
        return self.__height

    def add_disc(self, disc):
        """  get object from type disc and add it by the row and col to
        the board
        return True for success and False else"""
        row = disc.get_row()
        col = disc.get_col()
        if col not in range(WIDTH) or row not in range(HEIGHT):
            raise Exception("illegal move")
        self.__list_board[row][col] = disc.get_player()
        self.__discs.append(disc)

    def cell_content(self,row,col):
        """
        :param row and col are the coordinate we want to check
        :return: 1 for disc of player A, 2 for player B and None for empty cell
        """
        for disc in self.__discs:
            if row == disc.get_row() and col == disc.get_col():
                return disc.get_player()

    def top_in_col(self,col):
        """
        :param col: get a column
        :return: the indexes of the top empty cell in this column
        """
        save_row = self.__height
        for i in range(1, self.__height+1):
            row = self.__height - i
            if self.__list_board[row][col] is not None:
                save_row = row
        return save_row-1








