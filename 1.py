import numpy as np
import matplotlib.pyplot as plt
from math import cos,sin,pi,floor

def get_info_from_file(filepath):
  a = np.genfromtxt(filepath)
  t = a[:,0]
  x = a[:,1]
  return t,x


t1,x1 = get_info_from_file("python/utenfjar2.txt")
t2,x2 = get_info_from_file("python/utenfjar1.txt")
x1 /= 100
x2 /= 100

a1 = 2* (x1[-1] -x1[0])/(t1[-1] - t1[0])**2
a2 = 2* (x2[-1] -x2[0])/(t2[-1] - t2[0])**2
av = (a1+a2) / 2
vinkel = pi / 4
g = 9.82
my = av/(g*cos(vinkel))
print(my)