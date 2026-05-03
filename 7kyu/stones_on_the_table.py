# https://www.codewars.com/kata/5f70e4cce10f9e0001c8995a

stones = "RRRRGGGGBBBB"


def solution(stones):
    removeCounter = 0
    stonesList = list(stones)
    for i in range(len(stonesList) - 1):
        if stonesList[i] == stonesList[i + 1]:
            removeCounter += 1
    return removeCounter


print(solution(stones))
