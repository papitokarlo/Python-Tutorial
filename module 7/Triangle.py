#TASK 4 triangle oop: 
import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y
    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)
    def distance_from_point(self, point):
        return self.distance_from_xy(point.__x, point.__y)

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
       self.x =  vertice1
       self.y = vertice2
       self.z = vertice3

    def __str__(self):
        
        return f'{self.x}, {self.y}, {self.z}'
    
    def perimeter(self):
        perimeter = self.__x + self.__y + self.__z
        return perimeter


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle)
print(triangle.perimeter())