# https://www.codewars.com/kata/5262119038c0985a5b00029f
import math


def is_prime(num):
    if num < 0 or num == 0 or num == 1:
        return False
    elif num == 2:
        return True
    elif num > 2:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False

        return True
