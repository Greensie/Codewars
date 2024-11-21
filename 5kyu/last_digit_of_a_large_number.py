# https://www.codewars.com/kata/5511b2f550906349a70004e1
def last_digit(n1, n2):
    if n2 == 0:
        return 1

    temp = str(n1)
    b = int(temp[-1])
    r = n2 % 4
    if r == 0:
        r = 4
    ld = (b ** r) % 10
    return ld
