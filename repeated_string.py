#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    count=0
    t = ''
    for i in range(n*n):
        t=t+s

    for i in range(n):
        if t[i]=='a':
            count=count+1
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
