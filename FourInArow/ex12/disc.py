class Disc:

    def __init__(self, row, col, player):
        self.__col = col
        self.__row = row
        self.__player = player

    def get_col(self):
        """return the column"""
        return self.__col

    def get_row(self):
        """return the row"""
        return self.__row

    def get_player(self):
        """return the player"""
        return self.__player

