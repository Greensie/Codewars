# https://www.codewars.com/kata/51edd51599a189fe7f000015
import pytest


def solution(a1, a2):
    arr_len = len(a1)
    temp = 0
    for i in range(arr_len):
        absolute = 0
        absolute = (a1[i] - a2[i])
        absolute *= absolute
        temp += absolute

    return temp / arr_len


@pytest.mark.parametrize("tarr_a, tarr_b, expected_result",
                         [([1, 2, 3], [4, 5, 6], 9.0),
                          ([-1, 0], [0, -1], 1.0),
                          ([10, 10], [10, 10], 0),
                          ([10, 20, 10, 2], [10, 25, 5, -2], 16.5)])
def test_solution(tarr_a, tarr_b, expected_result):
    result = solution(tarr_a, tarr_b)
    assert result == expected_result
