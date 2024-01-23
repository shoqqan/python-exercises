# 1
import itertools
import random


def convert_grams(ounces):
    return ounces / 28.3495231


print(convert_grams(100))


# 2
def convert_to_celcium(farenheit):
    return (5 / 9) * (farenheit - 32)


# 3
all_legs = 94
all_heads = 35


def solve(numheads, numlegs):
    print("Rabits: ", (numlegs - (numheads * 2)) / 2)
    print("Chickens: ", numheads - ((numlegs - (numheads * 2)) / 2))


# 4
def filter_prime(list_numbers):
    prime_list = []

    for number in list_numbers:
        is_prime = True
        for i in range(2, int(number / 2) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(number)
    return prime_list


numbers = [1, 2, 3, 4, 5, 6, 7]
print(filter_prime(numbers))


# 5

def permutations(string):
    print(list(itertools.permutations(string)))


# 6

def reverse_sentence(sentence):
    reversed_sentence = sentence.split()
    return " ".join(reversed_sentence[::-1])


print(reverse_sentence("The quick brown fox"))


# 7

def has_33(nums):
    is_double3 = False
    for index, value in enumerate(nums):
        if index != 0 and nums[index - 1] == 3 and value == 3:
            is_double3 = True
            break
    return is_double3


# 8
def spy_game(nums):
    is_spy = False
    for index, value in enumerate(nums):
        if index > 1 and nums[index - 1] == 0 and nums[index - 2] == 0 and value == 7:
            return True
    return is_spy


# 9
def radius_from_spheres_volume(volume):
    return ((3 * volume) / (4 * 3.14)) ** (1 / 3)


# 10
new_collection = [1, 2, 2, 2, 3, 5, 7, 8, 8]


def without_repeats(collection):
    collection_without_repeats = []
    for num in collection:
        if num not in collection_without_repeats:
            collection_without_repeats.append(num)
    return collection_without_repeats


print(without_repeats(new_collection))


# 11
def is_palindrome(string):
    return string == string[::-1]


# 12

def histogram(list):
    for num in list:
        print("*" * num)


histogram([4, 9, 7])


# 13

def guess_the_number():
    name = input("Hello! What is your name? ")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    guess = int(input("Take a guess."))
    while True:
        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too much")
        else:
            print("Correct")
            break
        guess = int(input("Take a guess."))


# guess_the_number()


# 14
def function_wrapper(func):
    return func


function_wrapper(histogram([1, 4, 7]))
