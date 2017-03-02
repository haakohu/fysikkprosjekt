import numpy as np
import matplotlib.pyplot as plt
from math import cos,sin,pi,floor

def get_info_from_file(filepath):
  a = np.genfromtxt(filepath)
  t = a[:,0]
  x = a[:,1]
  return t,x



t,x = get_info_from_file("python/utenfjar2.txt")
x /= 100

n = len(t)
u = []
vinkel = pi/4
g = 9.81
half_size = floor(n/4)
t = t[half_size:n]
x = x[half_size:n]

for i in range(0,n-half_size):
  new_value = cos(vinkel) / sin(vinkel) - 2*x[i] / (g * t[i]**2 * sin(vinkel))
  u.append(new_value)




print(u)

print(np.average(u))
#plt.plot(t,u)
#plt.show()

