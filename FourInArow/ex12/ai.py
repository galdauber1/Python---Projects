import random


class AI:

    def __init__(self, game, player):
        self.__game = game
        self.__player = player

    def find_legal_move(self, timeout=None):
        """this func return the column of the legal move"""
        rand_lst=[]
        for col in range(7):
            if self.__game.get_player_at(0,col) is None:
                rand_lst.append(col)
        if rand_lst is None:
            raise Exception('NO possible AI moves')
        return random.choice(rand_lst)

    def get_last_found_move(self):
        pass
