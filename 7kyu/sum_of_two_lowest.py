#https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python

def sum_two_smallest_numbers(numbers):
    s_numbers = sorted(numbers)
    return s_numbers[0] + s_numbers[1]


numbers = [5, 8, 12, 18, 22]
print(sum_two_smallest_numbers(numbers))