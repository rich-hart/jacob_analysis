

import matplotlib.pyplot as plt

DATA_FILE_PATH = './Bimodal_Data.csv'


with open(DATA_FILE_PATH) as file:
    data = []
    for line in file:
        entries = line.split(',')
        first_entry = entries[0]
        try:
            value = float(first_entry)
        except ValueError:
            value = None
        if value is not None:
            data.append(value)


data.sort()
data_copy = data[:]

diff = []
value_a = data.pop(0)

while data:
    value_b = data.pop(0)
    diff.append(abs((float(value_b)-float(value_a))))
    value_a=value_b
    





y = diff
x = range(0,len(y))
deg = 4

from numpy import polyfit
from numpy.polynomial.polynomial import polyder
import numpy as np

poly=polyfit(x,y,deg)
poly = np.poly1d(poly)

der_poly = polyder(poly)
der_poly = np.poly1d(der_poly)

second_der_poly = polyder(der_poly)
second_der_poly = np.poly1d(second_der_poly)

local_max_min = der_poly.r

#print(local_max_min)
local_mins = []
local_max = []
for value in local_max_min:
    if second_der_poly(value)>0: #concave up
        local_mins.append(value)
    else:
        local_max.append(value)


local_mins.sort()
cluster_samples_1 = data_copy[0:int(local_max[0])]
cluster_samples_2 = data_copy[int(local_max[0]):len(data_copy)]

print("real sep point = "+str(max(cluster_samples_1)))


n, bins, patches = plt.hist(data_copy, 1000, normed=1, facecolor='green', alpha=0.75)



plt.xlabel('Seperation point: {0}'.format(max(cluster_samples_1)))
plt.show()

