import math
import os
import random
import re
import sys

def intgr(n):
    if n%2==1:
        print("Werid")
    elif n%2==1 and n in range(2,5):
        print("Not Weird")
    elif n%2==1 and n in range(6,20):
        print("Weird")
    elif n%2==0 and n>20:
        print("Not Weird")


if __name__ == '__main__':
    n = int(input().strip())
    intgr(n)