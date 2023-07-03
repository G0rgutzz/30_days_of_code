import math
import os
import random
import re
import sys


class VendingMachine:
    def __init__(self, num_items, item_coins, req_items, money):
        super().__init__()
        self.num_items = num_items
        self.item_coins = item_coins
        self.req_items = req_items
        self.money = money

    def buy(self, num_items, item_coins, req_items, money):
        num_price = req_items * item_coins
        if (money >= num_price) & (num_items >= req_items):
            num_items = num_items - req_items
            change = money - num_price
            return change, num_items
        elif num_items < req_items:
            return ValueError('Not enough items in the machine')
        elif money < num_price:
            return ValueError('Not enough coins')
    pass


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    while True:
        try:
            num_items, item_coins = map(int, input().split())
            n = int(input())
            req_items, money = map(int, input().split())
            machine = VendingMachine(num_items, item_coins, req_items, money)
        except EOFError:
            break
    for i in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")
    fptr.close()

