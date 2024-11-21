#https://www.codewars.com/kata/5270d0d18625160ada0000e4
def score(dice):
    num_counter = []
    value = 0
    i = 1
    while i <= 6:
        num_counter.append(dice.count(i))
        i += 1

    if num_counter[0] / 3 == 2:
        return 2000

    if num_counter[4] / 3 == 2:
        return 1000

    if num_counter[0] >= 3:
        value += 1000
        num_counter[0] -= 3
        if num_counter[0] <= 2:
            value += num_counter[0] * 100
    elif num_counter[0] <= 2:
        value += num_counter[0] * 100

    if num_counter[4] >= 3:
        value += 500
        num_counter[4] -= 3
        if num_counter[4] <= 2:
            value += num_counter[4] * 50
    elif num_counter[4] <= 2:
        value += num_counter[4] * 50

    for i in range(0, 6):
        if num_counter[i] >= 3:
            value += 100 * (i + 1)
            num_counter[i] -= 3

    return value
