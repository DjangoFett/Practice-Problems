"""
    Checks to see if a number is prime
"""
import math


def is_prime(number):
    """
    Brute force approach: get the square root of the number and loop
    through all possible factors. If the mod = 0, it is a factor and
    is not a prime number.
    :param number:
    :return:
    """
    x = int(math.sqrt(number)) + 1

    for i in range(x):
        print("factors: ", i, number)
        if number == i \
                or i == 1\
                or i == 0:
            continue

        if number % i == 0:
            print("factor: ", number, x)
            return False
    return True
