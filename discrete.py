import numpy as np
import random
import itertools
from scipy.stats import truncnorm
import matplotlib.pyplot as plt

''' gives a random index in the range 0 ... s for Normal distribution with mean m and deviation d'''
def get_normal_choice(s, m, d):
    size = 1000
    X = truncnorm(a=-s/2, b=s/2, loc=0, scale=d).rvs(size=size)
    X = X.round().astype(int)

    map = dict()
    for key, group in itertools.groupby(X):
        map[int(key + s / 2)] = map[int(key + s / 2)] + len(list(group)) if int(key + s / 2) in map else int(key + s / 2)

    p = [map[i] if i in map else 0 for i in range(s)]
    total = sum (p)
    p = [i/total for i in p]
    c = np.random.choice(list(range(s)), 1, p)
    index = int(m) + (c[0] - int(s/2)) - int (s/2) if int(m) + (c[0] - int(s/2)) > s else int(m) + (c[0] - int(s/2))
    #print (str(m) + ", " + str(d) + " := " + str(index))
    return list(range(s))[index-1]

