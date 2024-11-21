# https://www.codewars.com/kata/51e04f6b544cf3f6550000c1
def beeramid(bonus, price):
    if bonus < price:
        return 0
    cb = int(bonus / price)
    i = 1
    while cb > 0:
        cb -= i * i
        if cb < (i + 1) * (i + 1):
            break
        else:
            i += 1

    return i
