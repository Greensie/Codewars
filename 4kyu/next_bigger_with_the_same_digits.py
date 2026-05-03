# https://www.codewars.com/kata/next-bigger-number-with-the-same-digits
from pytest import mark


def next_bigger(n):
    if n < 10:
        return -1

    digits = list(str(n))
    biggerer_digits = []
    for i in range(len(digits) - 2, -1, -1):
        right_side = digits[i + 1 :]
        biggerer_digits = [d for d in right_side if d > digits[i]]
        if len(biggerer_digits) != 0:
            change = i
            break
    if not biggerer_digits:
        return -1
    swap_digit = min(biggerer_digits)
    for j in range(len(digits) - 1, change, -1):
        if digits[j] == swap_digit:
            digits[j], digits[change] = digits[change], digits[j]
            break
    digits[change + 1 :] = sorted(digits[change + 1 :])

    return int("".join(digits))


@mark.parametrize("n, exp", [(12, 21), (21, -1), (513, 531), (2017, 2071), (414, 441), (144, 414)])
def test_next_bigger(n, exp):
    assert next_bigger(n) == exp
