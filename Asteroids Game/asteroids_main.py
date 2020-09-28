from screen import Screen
import sys
import ship
import random
import math
from asteroid import Asteroid
from torpedo import Torpedo

DEFAULT_ASTEROIDS_NUM = 5
SHIP_MOVE = 7
SIZE3 = 3
SIZE2 = 2
SIZE1 = 1
SCORE = {'3':20, '2':50, '1':100}
MAX_TORPEDO = 10
MAX_LIFETIME = 200

#Messages:
END_ASTEROID_MSG = 'Success!! you destroyed all the asteroids!!!'
Q_MSG = 'you ask exit the game. bye bye'
END_LIFE_MSG = 'Your life is over :( \n bye bye...'
GAME_OVER = 'Game Over'
CRASH_MSG = " be careful next time!!, you crashed into asteroid"
CRASH_TITLE = ' crash alert '

class GameRunner:
    """"the class Gamerunner define the attributes that necessary for running
    a single game"""

    def __init__(self, asteroids_amount=DEFAULT_ASTEROIDS_NUM):
        """ a constructor for creating a gamerunner ship object"""
        self.__screen = Screen()
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self.__ship = ship.Ship(random.randint(self.__screen_min_x,
                    self.__screen_max_x), random.randint(self.__screen_min_y,
                                                       self.__screen_max_y))
        self.__asteroid_lst = []  # LIST OF ASTEROIDS
        self.__asteroids_amount = asteroids_amount
        self.__torpedo_lst = []
        self.__score = 0
        self.__shiplife = 3
        self.create_asteroids()


    def create_asteroids(self):
        """this function load asteroids into asteroids lst"""
        for i in range(self.__asteroids_amount):  # add asteroids to the list
            Asteroid.i = Asteroid(
                random.randint(self.__screen_min_x,self.__screen_max_x),
                        random.randint(self.__screen_min_y,self.__screen_max_y)
                                  , random.randint(1, 4), random.randint(1, 4))
            #  if the asteroid has the same location in x add one
            if Asteroid.i.get_x() == self.__ship.get_x():
                Asteroid.i.set_x(Asteroid.get_x() + 1)
            #  if the asteroid has the same location in y add one
            if Asteroid.i.get_y() == self.__ship.get_y():
                Asteroid.i.set_x(Asteroid.get_y() + 1)
            self.__asteroid_lst.append(Asteroid.i)
        for asteroid in self.__asteroid_lst:  # register asteroids
            self.__screen.register_asteroid(asteroid, SIZE3)

    def run(self):
        """run the game"""
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        """one iteration of the game -
        that define  the current location of all objects and check for
        keys pressing"""
        self.ship_drawing()
        self.asteroids_drawing()
        if self.__screen.is_space_pressed():
            self.create_torpedo()
        self.torpedo_drawing()
        self.if_key_pressed()
        msg = self.game_over()
        if msg is not None:
            self.__screen.show_message(GAME_OVER, msg)
            self.__screen.end_game()
            sys.exit()

    def ship_drawing(self):
        """draw the ship for the current loop"""
        self.x_new_loc(self.__ship)  # set the ship new loc in x
        self.y_new_loc(self.__ship)  # set the ship new loc in y
        self.__screen.draw_ship(self.__ship.get_x(), self.__ship.get_y(),
                                self.__ship.get_degrees())  # draw ship

    def asteroids_drawing(self):
        """create all the asteroids, register it and draw it in the game"""
        for asteroid in self.__asteroid_lst:  # draw asteroids
            self.__screen.draw_asteroid(asteroid, asteroid.get_x(),
                                        asteroid.get_y())
            self.y_new_loc(asteroid)
            self.x_new_loc(asteroid)
            if asteroid.has_intersection(self.__ship):  # checkforintersections
                self.asteroid_is_intersect(asteroid)
            for torpedo in self.__torpedo_lst:
                if asteroid.has_intersection(torpedo):
                    self.torpedo_is_intersect(torpedo,asteroid)

    def torpedo_drawing(self):
        """create the torpedos, register it and draw it in the game.
        remove them after 200 loops"""
        for torpedo in self.__torpedo_lst:
            self.__screen.draw_torpedo(torpedo, torpedo.get_x(),
                                       torpedo.get_y(),
                                       torpedo.get_degrees())
            self.y_new_loc(torpedo)
            self.x_new_loc(torpedo)
            torpedo.set_lifetime()
            if torpedo.get_lifetime() == MAX_LIFETIME:
                self.__screen.unregister_torpedo(torpedo)
                self.__torpedo_lst.remove(torpedo)

    def create_torpedo(self):
        """create the torpedo and register it"""
        if len(self.__torpedo_lst) < MAX_TORPEDO:
            torpedo = Torpedo(self.__ship.get_x(), self.__ship.get_y(),
                              self.__ship.get_degrees(),
                              self.__ship.get_speedx(),
                              self.__ship.get_speedy())
            self.__screen.register_torpedo(torpedo)
            self.__torpedo_lst.append(torpedo)

    def torpedo_is_intersect(self, torpedo, asteroid):
        """update data after torpedo intersected with asteroid"""
        for size, score in SCORE.items():
            if asteroid.get_size() == int(size):
                self.set_score(score)
                self.__screen.set_score(self.__score)
                if asteroid.get_size() != SIZE1:
                    self.change_size_asteroid(asteroid, torpedo)
                self.__screen.unregister_asteroid(asteroid)
                self.__asteroid_lst.remove(asteroid)

    def asteroid_is_intersect(self, asteroid):
        """update data after intersection between ship and asteroid"""
        self.__screen.show_message(CRASH_TITLE, CRASH_MSG)
        self.__screen.remove_life()
        self.set_shiplife()
        self.__screen.unregister_asteroid(asteroid)
        self.__asteroid_lst.remove(asteroid)

    def if_key_pressed(self):
        """check if some key was pressed and set the data by the pressing"""
        if self.__screen.is_left_pressed():
            self.__ship.set_degrees(SHIP_MOVE)  # move the ship degrees left
        elif self.__screen.is_right_pressed():  # move the ship degrees right
            self.__ship.set_degrees(-SHIP_MOVE)
        elif self.__screen.is_up_pressed():
            self.__ship.set_speed_x()
            self.__ship.set_speed_y()
        elif self.__screen.is_teleport_pressed():
            self.teleport_ship()

    def teleport_ship(self):
        """move the ship to random location"""
        x = random.randint(self.__screen_min_x, self.__screen_max_x)
        y = random.randint(self.__screen_min_x, self.__screen_max_x)
        while self.asteroid_exist(x, y):
            x = random.randint(self.__screen_min_x, self.__screen_max_x)
            y = random.randint(self.__screen_min_x, self.__screen_max_x)
        self.__ship.set_x(x)
        self.__ship.set_y(y)

    def asteroid_exist(self, x, y):
        """check if a asteroid exist in the input coordinates"""
        for asteroid in self.__asteroid_lst:
            if asteroid.get_x() == x and asteroid.get_y() == y:
                return True
        return False

    def set_score(self, score):
        """add the given score to the saved score"""
        self.__score += score

    def set_shiplife(self):
        """remove one life to the ship"""
        self.__shiplife -= 1

    def change_size_asteroid(self, asteroid, torpedo):
        """split the asteroid by his size"""
        speed_x, speed_y = self.update_asteroid_speed(asteroid, torpedo)
        size = asteroid.get_size()
        asteroid1 = Asteroid(asteroid.get_x(),asteroid.get_y(), speed_x,
                             speed_y, size-1)
        self.__asteroid_lst.append(asteroid1)
        asteroid2 = Asteroid(asteroid.get_x(), asteroid.get_y(), -speed_x,
                             -speed_y,size-1)
        self.__asteroid_lst.append(asteroid2)
        self.__screen.register_asteroid(asteroid1, asteroid1.get_size())
        self.__screen.register_asteroid(asteroid2, asteroid2.get_size())

    def update_asteroid_speed(self, asteroid, torpedo):
        """change the speed of the asteroid after the intersection"""
        speed_x = (torpedo.get_speedx()+asteroid.get_speedx())\
                 / math.sqrt((asteroid.get_speedx()**2+(asteroid.get_speedy())**2))
        speed_y = (torpedo.get_speedy()+asteroid.get_speedy())\
                 / math.sqrt((asteroid.get_speedx()**2+(asteroid.get_speedy())**2))
        return speed_x, speed_y

    def x_new_loc(self,flying_obj ):
        """update the location in x"""
        flying_obj.set_x((flying_obj.get_speedx() + flying_obj.get_x() - self.__screen_min_x) % \
        (self.__screen_max_x - self.__screen_min_x) + self.__screen_min_x)

    def y_new_loc(self, flying_obj):
        """update the location in x"""
        flying_obj.set_y((flying_obj.get_speedy() + flying_obj.get_y() - self.__screen_min_y) % \
            (self.__screen_max_y - self.__screen_min_y) + self.__screen_min_y)

    def game_over(self):
        """check if the game should over and return a message with the reason"""
        if len(self.__asteroid_lst) == 0:
            return END_ASTEROID_MSG
        if self.__shiplife == 0:
            return END_LIFE_MSG
        if self.__screen.should_end():
            return Q_MSG


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
