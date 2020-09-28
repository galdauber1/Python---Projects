import math
RADIUS = 1
RAD = 180
class Ship:
    """the class ship define the attributes of object from type ship
    for the asteroids game"""
    def __init__(self, x, y, speed_x=0, speed_y=0, degrees=0):
        """ a constructor for creating a single ship object"""
        self.__speed_x = speed_x
        self.__x = x
        self.__speed_y = speed_y
        self.__y = y
        self.__degrees = degrees
        self.__radius = RADIUS

    def get_degrees(self):
        """get the degrees"""
        return self.__degrees

    def set_degrees(self, degrees):
        """add degrees"""
        self.__degrees += degrees

    def set_speed_x(self):
        """add speed to ship in x"""
        self.__speed_x += math.cos((self.__degrees * math.pi)/RAD)

    def set_speed_y(self):
        """add speed to shipn in y"""
        self.__speed_y += math.sin((self.__degrees * math.pi)/RAD)

    def set_x(self, x):
        """set new x location"""
        self.__x = x

    def set_y(self, y):
        """set new y location"""
        self.__y = y


    def get_x(self):
        """get the x location"""
        return self.__x

    def get_y(self):
        """get y location"""
        return self.__y

    def get_speedx(self):
        """get speed_x"""
        return self.__speed_x

    def get_speedy(self):
        """get speed_Y"""
        return self.__speed_y

    def get_radius(self):
        return self.__radius
