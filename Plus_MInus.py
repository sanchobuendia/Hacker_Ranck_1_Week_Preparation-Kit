# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
# Print the decimal value of each fraction on a new line with places after the decimal.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive = round(len(list(filter(lambda pos: pos > 0, arr)))/len(arr),6)
    negative = round(len(list(filter(lambda negative: negative < 0, arr)))/len(arr),6)
    zero = round(len(list(filter(lambda zero: zero == 0, arr)))/len(arr),6)
    return print(str(positive) + '\n' + str(negative) + '\n' + str(zero))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
