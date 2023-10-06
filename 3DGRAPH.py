# Libraries needed in 

import numpy as np
#import matplotlib.pyplot as plt

data = open('DistList-20230905-232221.csv', 'r')
data = data.readlines()
GPS = []

for line in data:
    if line[-13]