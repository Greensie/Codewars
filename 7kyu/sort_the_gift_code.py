# https://www.codewars.com/kata/52aeb2f3ad0e952f560005d3
def sort_gift_code(code):
    x = sorted(code)
    y = ''
    for i in range(0, len(x)):
        y += x[i]
    return y
