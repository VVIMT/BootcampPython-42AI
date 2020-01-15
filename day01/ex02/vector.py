import math
import numpy

class Vector:
    def __init__(self, param = None):
        self.values = []
        self.size = 0

        if type(param) == list:
            for elem in param:
                if type(elem) != float:
                    raise Exception
            self.values = param
        
        elif type(param) == int or type(param) == float:
            self.values = list(numpy.arange(float(0), float(param), 1))
        
        elif type(param) == tuple:
            self.values = list(numpy.arange(float(param[0]), float(param[1]), 1))
        
        else:
            raise Exception("Error: bad parameter type")