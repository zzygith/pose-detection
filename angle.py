import math
import numpy as np
 

class Point(object):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
 
    def vector(self):
        c = (self.x1 - self.x2, self.y1 - self.y2)
        return c
 
    def length(self):
        d = math.sqrt(pow((self.x1 - self.x2), 2) + pow((self.y1 - self.y2), 2))
        return d

class Calculate(object):
    def __init__(self, x, y, m, n):
        self.x = x
        self.y = y
        self.m = m
        self.n = n
 
    def Vector_multiplication(self):
        self.mu = np.dot(self.x, self.y)
        return self.mu
 
    def Vector_model(self):
        self.de = self.m * self.n
        return self.de
 
    def cal(self):
        result = math.acos(Calculate.Vector_multiplication(self) / Calculate.Vector_model(self))*180/3.1415926
        result = round(result,1)
        return result
 


def ag(a,n):

    angle_result = np.zeros((n,4))

    for i in range(n):
        if a[i][0][1] == 0 or a[i][0][2] == 0:  
            first_line = Point(a[i][0][0], a[i][1][0], a[i][0][1]+a[i][0][2], a[i][1][1]+a[i][1][2]) # Neck to Hip (average of Left Hip and Right Hip)
        else:
            first_line = Point(a[i][0][0], a[i][1][0], (a[i][0][1]+a[i][0][2])/2, (a[i][1][1]+a[i][1][2])/2)
        second_line = Point(a[i][0][0], a[i][1][0], a[i][0][3], a[i][1][3]) # Neck to Nose
        ca = Calculate(first_line.vector(), second_line.vector(), first_line.length(), second_line.length())
        
        angle_result[i]=[i, a[i][0][0], a[i][1][0],  ca.cal()] #store the neck coordinate and responding angle

    return(angle_result)