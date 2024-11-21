#https://www.codewars.com/kata/5715eaedb436cf5606000381
def positive_sum(arr):
    if len(arr) == 0:
        return 0
    sum = 0
    for el in arr:
        if el > 0:
            sum += el
    return sum