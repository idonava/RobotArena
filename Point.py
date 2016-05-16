import math


class Point(object):
    '''Creates a point on a coordinate plane with values x and y.'''

    COUNT = 0

    def __init__(self, x, y):
        '''Defines x and y variables'''
        self.X = x
        self.Y = y


    def __str__(self):
        return "Point(%s,%s)"%(self.X, self.Y)