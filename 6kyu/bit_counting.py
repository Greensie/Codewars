# https://www.codewars.com/kata/526571aae218b8ee490006f4
def count_bits(n):
    x = bin(n)
    tab = []
    for letters in x:
        tab += letters
    tab.pop(0)
    tab.pop(0)
    ret = tab.count("1")
    return ret
