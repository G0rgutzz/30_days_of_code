import math
import os
import random
import re
import sys

n = int(input().strip())
a = list(map(int, input().rstrip().split()))
num_swaps = 0
for i in range(n):
    for j in range(n-1):
        if a[j] > a[j+1]:
            tmp = a[j]
            a[j] = a[j+1]
            a[j+1] = tmp
            num_swaps += 1
    if num_swaps == 0:
        break

print("Array is sorted in"+num_swaps+"ways")
print("First element: "+a[0])
print("Last element: "+a[len(a)-1])
