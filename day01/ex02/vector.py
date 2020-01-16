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
                    if type(elem) == int or type(elem) == float:
                        elem = float(elem)
                    else:
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
        x = []

        if isinstance(other, list):
            if self.size == len(other):
                for i in range(0, self.size):
                    x.append(self.values[i] + other[i])
            else:
                print("Both operands must have the same dimensions.\n")
        elif isinstance(other, type(self)):
            if self.size == other.size:
                for i in range(0, self.size):
                    x.append(self.values[i] + other.values[i])
            else:
                print("Both operands must have the same dimensions.\n")
        elif isinstance(other, int) or isinstance(other, float):
            if self.size == 1:
                x.append(self.values[0] + other)
            else:
                print("Both operands must have the same dimensions.\n")
        else:
            pass
        return x

    def __radd__(self, other):
        x = []

        if isinstance(other, list):
            if self.size == len(other):
                for i in range(0, self.size):
                    x.append(self.values[i] + other[i])
            else:
                print("Both operands must have the same dimensions.\n")
        elif isinstance(other, int) or isinstance(other, float):
            if self.size == 1:
                x.append(self.values[0] + other)
            else:
                print("Both operands must have the same dimensions.\n")
        else:
            pass
        return x

    def __sub__(self, other):        
        x = []

        if isinstance(other, list):
            if self.size == len(other):
                for i in range(0, self.size):
                    x.append(self.values[i] - other[i])
            else:
                print("Both operands must have the same dimensions.\n")
        elif isinstance(other, type(self)):
            if self.size == other.size:
                for i in range(0, self.size):
                    x.append(self.values[i] - other.values[i])
            else:
                print("Both operands must have the same dimensions.\n")
        elif isinstance(other, int) or isinstance(other, float):
            if self.size == 1:
                x.append(self.values[0] - other)
            else:
                print("Both operands must have the same dimensions.\n")
        else:
            pass
        return x

    def __rsub__(self, other):
        x = []

        if isinstance(other, list):
            if self.size == len(other):
                for i in range(0, self.size):
                    x.append(- self.values[i] + other[i])
            else:
                print("Both operands must have the same dimensions.\n")
        elif isinstance(other, int) or isinstance(other, float):
            if self.size == 1:
                x.append(- self.values[0] + other)
            else:
                print("Both operands must have the same dimensions.\n")
        else:
            pass
        return x

    def __truediv__(self, other):
        x = []

        if isinstance(other, int) or isinstance(other, float):
            if self.size == 1:
                try:
                    if other != 0:
                        x.append(self.values[0] / other)
                    else:
                        raise ZeroDivisionError
                except ZeroDivisionError:
                    print("ZeroDivisionError")
        else:
            print("TypeError: unsupported operand type(s)")
        return x

    def __rtruediv__(self, other):
        x = []

        if isinstance(other, list):
            if self.size == len(other):
                for i in range(0, self.size):
                    try:
                        if other[i] != 0:
                            x.append(self.values[i] / other[i])
                        else:
                            raise ZeroDivisionError
                    except ZeroDivisionError:
                        print("ZeroDivisionError")
        elif isinstance(other, int) or isinstance(other, float):
            if self.size == 1:
                try:
                    if other != 0:
                        x.append(self.values[0] / other)
                    else:
                        raise ZeroDivisionError
                except ZeroDivisionError:
                    print("ZeroDivisionError")
        else:
            pass
        return x

    def __mul__(self, other):
        x = []

        if isinstance(other, list):
            if self.size == len(other):
                for i in range(0, self.size):
                    x.append(self.values[i] * other[i])
        elif isinstance(other, type(self)):
            if self.size == other.size:
                for i in range(0, self.size):
                    x.append(self.values[i] * other.values[i])
        elif isinstance(other, int) or isinstance(other, float):
            if self.size == 1:
                x.append(self.values[0] * other)
        else:
            pass
        return x

    def __rmul__(self, other):
        x = []

        if isinstance(other, list):
            if self.size == len(other):
                for i in range(0, self.size):
                    x.append(self.values[i] * other[i])
        elif isinstance(other, int) or isinstance(other, float):
            if self.size == 1:
                x.append(self.values[0] * other)
        else:
            pass
        return x

    def __str__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])

        pass
    def __repr__(self):