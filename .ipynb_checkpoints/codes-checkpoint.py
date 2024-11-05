# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

def g(n):
    # X = 
    if  n == 1:
        return np.array([0,1])
    else:
        return np.concatenate((g(n-1) , np.array([10**(n-1) + i for i in g(n-1)])))

g(4)









