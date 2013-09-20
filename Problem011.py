from numpy import loadtxt
import os
dir = os.path.dirname(__file__)

data = loadtxt(os.path.join(dir,"Problem011_data.txt"), delimiter=' ')
print(data[0][0])