import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input("podaj liczbę: ").strip())
    maximum = 0
    ilosc = 0
    kod = ""
    kod1 = ""
    while n > 0:
        if n % 2 == 1:
            kod += "1"
        else:
            kod += "0"
        n = round(n//2)
        print(n)
    print(kod)

    for i in range(0, len(kod)):
        kod1 += kod[-i-1]
    print(kod1)
    for j in range(0, len(kod1)):
        if kod1[j] == "1":
            ilosc += 1
            if ilosc > maximum:
                maximum = ilosc
        else:
            ilosc = 0
    print(maximum)
