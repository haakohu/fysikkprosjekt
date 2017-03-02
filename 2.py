import numpy as np
import matplotlib.pyplot as plt
from math import cos,sin,pi,floor

def get_info_from_file(filepath):
  a = np.genfromtxt(filepath)
  t = a[:,0]
  x = a[:,1]
  return t,x



t,x = get_info_from_file("python/fjar1.txt")

x /= 100

n = len(x)
v = [0]
a = [0,0]
m = 0.256
g = 9.81
vinkel = pi / 4
delta_t = t[-1] / n
v = [0]
#g = lambda i: m * g*(cos(vinkel) - u * sin(vinkel)) - 
for i in range(1,n):
  new_value = x[i] - x[i-1]
  new_value /= delta_t
  v.append(new_value)
  
for i in range(1,n-1):
  new_value = v[i] - v[i-1]
  a.append(new_value / delta_t)



# plt.plot(t,v)
plt.plot(t,v)
print(np.average(a))
plt.show()