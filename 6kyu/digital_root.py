# https://www.codewars.com/kata/541c8630095125aba6000c00
def digital_root(n):
    if n < 10:
        return n

    A = [int(x) for x in str(n)]
    total = sum(A)

    if total < 10:
        return total
    else:
        return digital_root(total)
