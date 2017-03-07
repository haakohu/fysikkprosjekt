import numpy as np
import matplotlib.pyplot as plt
from math import cos,sin,pi,floor, sqrt, inf
from my_finder import *

def get_info_from_file(filepath):
  a = np.genfromtxt(filepath)
  t = a[:,0]
  x = a[:,1]
  return t,x

def get_turning_point(x):
  turning_point = -5
  N = len(x)
  for i in range(1,N):
    if x[i] > x[i-1]:
      turning_point = i
  return turning_point


t,x = get_info_from_file("python/fjar1.txt")
x /= 100
turning_point = get_turning_point(x)

m = 0.256
g = 9.81
vinkel = pi / 4
my = get_my(g)

G  = lambda x,k: g*(sin(vinkel) - my*cos(vinkel)) - (k * x / m)

def get_new_x(x,t,k):
  x_numerical = [x[0]]
  v_numerical = [0]
  N = len(x)
  delta_t = t[-1] / N
  for i in range(0,N-1):
    v_first = v_numerical[i] + delta_t/2.0 * G(x_numerical[i],k)
    x_new = x[i] + v_first*delta_t
    v_second = v_first + delta_t/2.0*G(x_new,k)
    x_numerical.append(x_new)
    v_numerical.append(v_second)
    errors = []
  return x_numerical

def get_error(x_num, x):
  error = 0
  N = len(x)
  for i in range(len(x)):
    error += (x[i] - x_num[i])**2
  error = sqrt(error/N)
  return error

def find_k_with_lowest_error(x,t):
  min_error = inf
  min_k = 0
  for k in range(1000):
    x_numerical = get_new_x(x,t,k)
    error = get_error(x_numerical,x)
    if error  < min_error:
      min_error = error
      min_k = k
  print("LOWEST ERRROR K IS")
  print("Error = " + str(min_error))
  print("K is: " + str(min_k))


def plot(x,t,k):
  x_num = get_new_x(x,t,k)
  plt.plot(t,x,t,x_num)
  plt.legend(['Measured data','calculated data'])
  plt.show()

# find_k_with_lowest_error(x,t)
plot(x,t,40)