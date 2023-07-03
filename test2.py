import pylab
import math


def gunwo():
    s = str(input())
    k = len(s)
    a = ""
    if k % 2 == 0:
        j = int(k/2)
        for i in range(0, j):
            # print("%s" % s[2*i])
            a = a + s[2*i]
        a = a + " "
        for i in range(0, j):
            # print("%s" % s[2*i+1])
            a = a + s[2*i+1]
    else:
        j = int((k+1)/2)
        for i in range(0, j):
            # print("%s" % s[2*i])
            a = a + s[2*i]
        a = a + " "
        for i in range(1, j):
            # print("%s" % s[2*i-1])
            a = a + s[2*i-1]
    print(j)
    print(k, "\n")
    print(a)
    return 0


gunwo()
