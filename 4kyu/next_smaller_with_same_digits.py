# https://www.codewars.com/kata/5659c6d896bc135c4c00021e
from pytest import mark


def next_smaller(n):
    if n < 10:
        return -1

    digits = list(str(n))
    smaller_digits = []
    for i in range(len(digits) - 2, -1, -1):
        right_side = digits[i + 1 :]
        smaller_digits = [d for d in right_side if d < digits[i]]
        if len(smaller_digits) != 0:
            change = i
            break
    if not smaller_digits:
        return -1
    swap_digit = max(smaller_digits)
    for j in range(len(digits) - 1, change, -1):
        if digits[j] == swap_digit:
            digits[j], digits[change] = digits[change], digits[j]
            break
    digits[change + 1 :] = sorted(digits[change + 1 :], reverse=True)
    if digits[0] == "0":
        return -1

    return int("".join(digits))


@mark.parametrize(
    "n, exp",
    [
        (907, 790),
        (531, 513),
        (135, -1),
        (2071, 2017),
        (414, 144),
        (123456798, 123456789),
        (123456789, -1),
        (1234567908, 1234567890),
    ],
)
def test_next_smaller(n, exp):
    assert next_smaller(n) == exp
