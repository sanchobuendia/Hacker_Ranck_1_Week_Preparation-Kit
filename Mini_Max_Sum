# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.

#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    def soma(l):
        r = sum(l)
        return r
        
    combinations = list(itertools.combinations(arr, 4))
    maxr = max(list(map(soma, combinations)))
    minr = min(list(map(soma, combinations)))
    
    return print(str(minr) + ' ' + str(maxr))
    #return print(maxr)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
