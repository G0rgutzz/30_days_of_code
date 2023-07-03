import math
import os
import random
import re
import sys

a = ""
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    # print(arr)
    for i in range(0, n):
        a = a + " " + str(arr[n-i-1])
    print(a.strip())
