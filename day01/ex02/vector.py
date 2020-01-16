import math
import numpy

class Vector:
    def __init__(self, param = None):
        self.values = []
        self.size = 0
        self.total = 0
        try:
            if type(param) == list:
                for elem in param:
                    if type(elem) != float:
                        raise TypeError
                self.values = param
            elif type(param) == int or type(param) == float:
                self.values = list(numpy.arange(float(0), float(param), 1))
            elif type(param) == tuple:
                self.values = list(numpy.arange(float(param[0]), float(param[1]), 1))
            else:
                raise TypeError
            self.size = len(self.values)
        except TypeError:
            print("Error: bad parameter type")

    def __add__(self, other):
        return other + self.values

    def __radd__(self, other):
        x = []
        if self.size == other.size:
            for i in range(0, self.size):
                x.append(self.values[i] + other.values[i])
        return x

    def __sub__(self):
        pass

    def __rsub__(self):
        pass

    def __truediv__(self):
        pass
    
    def __rtruediv__(self):
        pass

    def __mul__(self):
        pass

    def __rmul__(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass