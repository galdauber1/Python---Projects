TWO = 2
RADIUSIZE = 10
FIVE = 5
import math
class Asteroid:
    """the class asteroid define the attributes of object from type asteroid
        for the asteroids game"""
    def __init__(self, x, y, speed_x, speed_y, size=3):
        """ a constructor for creating a single asteroid object"""
        self.__speed_x = speed_x
        self.__x = x
        self.__speed_y = speed_y
        self.__y = y
        self.__size = size
        self.__radius = size*RADIUSIZE - FIVE

    def get_x(self):
        """get x location"""
        return self.__x

    def get_y(self):
        """get y location"""
        return self.__y

    def get_speedx(self):
        """get speed_y"""
        return self.__speed_x

    def get_speedy(self):
        """get speed_x"""
        return self.__speed_y

    def set_x(self, x):
        """set x location"""
        self.__x = x

    def set_y(self, y):
        """set y location"""
        self.__y = y

    def get_size(self):
        return self.__size

    def has_intersection(self, obj):
        """check if there is intersection"""
        distance = math.sqrt((obj.get_x() - self.__x)**TWO +
                             (obj.get_y() - self.__y)**TWO)
        if distance <= self.__radius + obj.get_radius():
            return True
        return False


