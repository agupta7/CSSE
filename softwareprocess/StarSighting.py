import math

class StarSighting(object):
    def __init__(self, degrees, minutes):
        self._degrees = degrees
        self._minutes = minutes

    def getDegrees(self):
        return self._degrees
    
    def getMinutes(self):
        return self._minutes