# https://www.codewars.com/kata/5a4138acf28b82aa43000117
import pytest

a = [1, 2, 3]


def adjacent_element_product(array):
    res = -10000000000000000000
    for i in range(len(array) - 1):
        temp = array[i] * array[i + 1]
        if temp > res:
            res = temp
        else:
            continue
    return res


print(adjacent_element_product(a))


@pytest.mark.parametrize("arr, expected_result", [
    ([5, 8], 40),
    ([1, 2, 3], 6),
    ([1, 5, 10, 9], 90),
    ([4, 12, 3, 1, 5], 48),
    ([9, 5, 10, 2, 24, -1, -48], 50),
    ([1, 0, 1, 0, 1000], 0),
    ([-23, 4, -5, 99, -27, 329, -2, 7, -921], -14)
])
def test_arrays(arr, expected_result):
    assert adjacent_element_product(arr) == expected_result
