import math
RAD = 180
RADIUS = 4


class Torpedo:
    """"the class torpedo define the attributes of object from type torpedo
    for the asteroids game"""
    def __init__(self, x, y, degrees, speed_x=0, speed_y=0):
        """ a constructor for creating a torpedo ship object"""
        self.__x = x
        self.__y = y
        self.__degrees = degrees
        self.__radius = 4
        self.__speed_y = speed_y + 2 * math.sin((degrees * math.pi)/RAD)
        self.__speed_x = speed_x + 2 * math.cos((degrees * math.pi)/RAD)
        self.__lifetime = 0


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

    def set_degrees(self, deg):
        """set the degrees"""
        self.__degrees = deg

    def get_degrees(self):
        """return the degrees"""
        return self.__degrees

    def get_radius(self):
        """return the radius"""
        return self.__radius

    def set_lifetime(self):
        """add 1 life to the life time"""
        self.__lifetime += 1

    def get_lifetime(self):
        """return lifetime"""
        return self.__lifetime
