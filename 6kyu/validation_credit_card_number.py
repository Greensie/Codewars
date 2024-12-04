# https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2
import pytest

n = 17855


def validate(n):
    result = 0
    tab = [int(x) for x in str(n)]
    if len(tab) % 2 == 0:
        for i in range(len(tab)):
            if i % 2 == 0:
                tab[i] = 2 * tab[i]
                if tab[i] > 9:
                    tab[i] = check_for_doubledigits(tab[i])
            result += tab[i]
        if result % 10 == 0:
            return True
        else:
            return False

    else:
        for i in range(len(tab)):
            if i % 2 == 1:
                tab[i] = 2 * tab[i]
                if tab[i] > 9:
                    tab[i] = check_for_doubledigits(tab[i])
            result += tab[i]
        if result % 10 == 0:
            return True
        else:
            return False


def check_for_doubledigits(num):
    temp = [int(x) for x in str(num)]
    sum = int(temp[0]) + int(temp[1])
    return sum


# print(validate(n))
@pytest.mark.parametrize("numbers, expected_result", [
    (1714, False),
    (12345, False),
    (891, False),
    (1, False),
    (2121, True),
    (1230, True),
])
def test_solution(numbers, expected_result):
    assert validate(numbers) == expected_result
