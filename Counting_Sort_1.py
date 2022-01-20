# Quicksort usually has a running time of , but is there an algorithm that can sort even faster?
# In general, this is not possible. Most sorting algorithms are comparison sorts, i.e. 
# they sort a list just by comparing the elements to one another. A comparison sort algorithm cannot beat  
# (worst-case) running time, since  represents the minimum number of comparisons needed to know where to place each element.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    cem = list(range(0,100))
    res = []
    for i in cem:
        cc = 0
        for j in range(len(arr)):
            if arr[j] == i:
                cc += 1
        res.append(cc)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
