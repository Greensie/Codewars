# https://www.codewars.com/kata/514b92a657cdc65150000006
def solution(number):
    A = []
    for i in range(1, number):
        if i % 3 == 0:
            A.append(i)
        elif i % 5 == 0 and i not in A:
            A.append(i)
    total = sum(A)
    return total
