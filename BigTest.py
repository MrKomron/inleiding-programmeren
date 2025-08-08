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




# Vraag 2
# Vraag 3
# Vraag 4
# Vraag 5