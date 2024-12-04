# https://www.codewars.com/kata/52761ee4cffbc69732000738
a1 = '1 1 1 1 1 1'
a2 = '1 1 1 1 1 1 1'

def good_vs_evil(good, evil):
    good_dict = {0: 1, 1: 2, 2: 3, 3: 3, 4: 4, 5: 10} #position in str: worth
    evil_dict = {0: 1, 1: 2, 2: 2, 3: 2, 4: 3, 5: 5, 6: 10}
    sumg,sume = 0,0
    g = good.split(" ")
    e = evil.split(" ")
    for i in range(len(g)):
        sumg += int(g[i]) * good_dict.get(i)

    for i in range(len(e)):
        sume += int(e[i]) * evil_dict.get(i)

    if sumg > sume:
        retstr = "Battle Result: Good triumphs over Evil"
    elif sume > sumg:
        retstr = "Battle Result: Evil eradicates all trace of Good"
    else:
        retstr = "Battle Result: No victor on this battle field"
    return retstr

