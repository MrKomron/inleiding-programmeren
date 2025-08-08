# Vraag 1
from math import sqrt

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def print(self):
        print(self.x,self.y)

    def reflect_x(self):
        return Point(self.x,-self.y)

    def distance(self,Point):
        result=sqrt((self.x-Point.x)**2+(self.y-Point.y)**2)
        return result

    def compute_line_to(self,other):
        a=(self.y-other.y)/(self.x-other.x)
        b=other.y-a*other.x
        return (a,b)

class Rectangle:
    def __init__(self, corner, width, height):
        self.corner=corner
        self.width=width
        self.height=height
    def area(self):
        result=self.width*self.height
        return result

    def equals(self,other):
        if self.width==other.width and self.height==other.height and self.corner.x==other.corner.x and self.corner.y==other.corner.y:
            return True
        else:
            return False






# Vraag 2
# Vraag 3
# Vraag 4
# Vraag 5