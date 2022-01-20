# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock. 
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    
    if s[-2::] == 'AM':
        s = s[:8]
        s2 = s.split(":")
        if int(s2[0]) == 12:
            s2[0] = "%02d" % (int(s2[0]) - 12)
            s = ':'.join(s2)
        if int(s2[0]) != 12:
            s2[0] = "%02d" % (int(s2[0]))
            s = ':'.join(s2)
        
    if s[-2::] == 'PM':
        s = s[:8]
        s2 = s.split(":")
        if int(s2[0]) == 12:
            s2[0] = "%02d" % (int(s2[0]) - 12)
            s = ':'.join(s2)
        if int(s2[0]) != 12:
            s2[0] = "%02d" % (int(s2[0]) + 12)
            s = ':'.join(s2)
        
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
