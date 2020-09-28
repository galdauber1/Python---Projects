from .board import Board
from .disc import Disc

PLAYER_A = 1
PLAYER_B = 2
POS_NEG = [-1,1]
FOUR_A ='1111'
FOUR_B = '2222'


class Game:

    def __init__(self):
        self.__counter_steps = 0
        self.__board = Board()
        self.__current_cell = [0,0]
        self.__lst_four = []

    def make_move(self, column):
        """
        make on move of the game
        :param column: The column the player want to insert a disc
        :return:
        """
        try:
            self.__counter_steps += 1
            row = self.__board.top_in_col(column)
            self.__current_cell = [row,column]
            self.__board.add_disc(Disc(row, column, self.get_current_player()))
        except Exception:
            self.__counter_steps -= 1
            raise Exception('illegal move')

        if self.get_winner() is not None:
            return self.__lst_four

    def valid_column(self, col):
        """check if the col in the domain, if the col isn't full or if
        the game is over"""
        if col not in range(self.__board.get_width()) or \
                self.__board.top_in_col(col)[0] == -1:
                return False
        return True

    def get_winner(self):
        """
        :return: 1 if player A is the winner, 2 if player B, 0 if the board
        is full and there is no winner and None if the game is not over yet.
        """
        row = self.__current_cell[0]
        col = self.__current_cell[1]
        if self.four_in_a_col(col) or self.four_in_a_row(row) or \
                self.four_in_a_diagonal(row,col) :
            return self.get_current_player()
        elif self.__board.board_is_full():
            return 0
        else:
            return None

    def four_in_a_row(self, row):
        """
        get the row of the last disc that was insert to the board and return if
        it make set of four discs of the same player in the current row
        """
        count = 0
        for col in range(self.__board.get_width()):
            if self.__board.get_list_board()[row][col] == \
                    self.get_current_player():
                count += 1
                self.__lst_four.append([row,col])
                if count == 4:
                    return True
            else:
                count = 0
                self.__lst_four = []
        return False

    def four_in_a_col(self, col):
        """
        get the col of the last disc that was insert to the board and return if
        it make set of four discs of the same player in the current col
        """
        count = 0
        for row in range(self.__board.get_height()):
            if self.__board.get_list_board()[row][col] == self.get_current_player():
                count += 1
                self.__lst_four.append([row,col])
                if count == 4:
                    return True
            else:
                count = 0
                self.__lst_four = []
        return False

    def four_in_a_diagonal(self, row, col):
        """get the col of the last disc that was insert to the board and return if
        it make set of four discs of the same player in the diagonal"""
        width = self.__board.get_width()
        height = self.__board.get_height()
        cur_player = str(self.get_current_player())*4
        lst1=[]
        lst2=[]
        lst3=[]
        lst4=[]
        count1=1
        count2=1
        count3=1
        count4=1
        row1 = row
        col1 = col
        while row1 in range(height) and col1 in range(width) and count1<4:
            lst1.append( str(self.__board.get_list_board()[row1][col1]))
            row1 += 1
            col1+=1
            count1+=1
        row2 = row
        col2 = col
        while row2 in range(height) and col2 in range(width) and count2<4:
            lst2.append( str(self.__board.get_list_board()[row2][col2]))
            row2 -= 1
            col2 -= 1
            count2 +=1
        row3 = row
        col3 = col
        while row3 in range(height) and col3 in range(width) and count3<4:
            lst3.append( str(self.__board.get_list_board()[row3][col3]))
            row3 -= 1
            col3+= 1
            count3+=1
        row4 = row
        col4 = col
        while row4 in range(height) and col4 in range(width) and count4<4:
            lst4.append( str(self.__board.get_list_board()[row4][col4]))
            row4 += 1
            col4-= 1
            count4+=1
        lst5 = lst2[:]+lst1[1:]
        lst6 = lst4[:]+lst3[1:]
        string3 =''.join(lst5)
        string4 =''.join(lst6)
        if cur_player in string4:
            self.__lst_four=[[row4-1,col4+1],[row4-2,col4+2],[row4-3,col4+3],
                             [row4-4,col4+4]]
            return True
        elif cur_player in string3:
            self.__lst_four=[[row2+1,col2+1],[row2+2,col2+2],[row2+3,col4+3],
                             [row2+4,col4+4]]
            return True
        else:
            self.__lst_four=[]
            return False

    def get_row(self):
        """get the row"""
        return self.__current_cell[0]

    def get_counter(self):
        """get the step counter"""
        return self.__counter_steps

    def set_counter(self):
        """add 1 to counter"""
        self.__counter_steps +=1

    def get_player_at(self, row, col):
        """
        :param row and col of a current cell
        :return: the player who own the disc in this cell
        """
        return self.__board.get_list_board()[row][col]

    def get_current_player(self):
        """
        :return: 1 for player A or 2 for player B
        """
        if self.__counter_steps == 0:
            return PLAYER_A

        elif self.__counter_steps % 2 == 0:
            return PLAYER_B
        return PLAYER_A

