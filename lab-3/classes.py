# 1
import math


class Strings:
    def __init__(self):
        self.string = "lol"

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())


# 2,3
class Shape:
    def __init__(self):
        self.area = 0

    class Square:
        def __init__(self, length):
            self.length = length

        def area(self):
            return self.length ** 2

    @property
    def area(self):
        return self.area

    class Rectangle:
        def __init__(self, length, width):
            self.length = length
            self.width = width

        def area(self):
            return self.length * self.width


# 4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self, x, y):
        self.x = x
        self.y = y

    def dist(self, second_x, second_y):
        return (((self.x - second_x) ** 2) + ((self.y - second_y) ** 2)) ** (1 / 2)


# 5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, count):
        self.balance += count

    def withdraw(self, count):
        if count > self.balance:
            print('You do not have enough')
        else:
            self.balance -= count


# 6
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def filter_list(list_for_filter):
    return list(filter(lambda x: is_prime(x), list_for_filter))
