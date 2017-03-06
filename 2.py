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

N = len(x)
v = [0]
a = [0,0]
m = 0.256
g = 9.81
vinkel = pi / 4
delta_t = t[-1] / N
my = 0.583141176884
k = 65
print(N)
x_numerical = [x[0]]
v_numerical = [0]
G_first = lambda x: (m*g*sin(vinkel) + my*m*g*cos(vinkel) - k * x) / m
G_last  = lambda x: (m*g*sin(vinkel) - my*m*g*cos(vinkel) - k * x) / m
#Finne når klossen endrer retning
turning_point = -5

for i in range(1,N):
  if x[i] > x[i-1]:
    turning_point = i
    break
print(turning_point)

for i in range(0,turning_point):
  x_numerical.append(x_numerical[-1] + delta_t * v_numerical[-1])
  v_numerical.append(v_numerical[-1] + delta_t * G_first(x_numerical[-2]))

for i in range(turning_point,N):
  x_numerical.append(x_numerical[-1] + delta_t * v_numerical[-1])
  v_numerical.append(v_numerical[-1] + delta_t * G_last(x_numerical[-2]))

# plt.plot(t,v)
print(x_numerical)
plt.plot(t,x_numerical[0:-1])
plt.plot(t,x)
print(np.average(a))
plt.show()