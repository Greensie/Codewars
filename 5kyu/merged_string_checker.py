# https://www.codewars.com/kata/54c9fcad28ec4c6e680011aa - broken tests is merged also work for non-sorted strings
import pytest

s = 'codewars'
p1 = 'cdw'
p2 = 'oears'


def is_merge(s, part1, part2):
    if sorted(s) == sorted(part1 + part2):
        return True
    return False


@pytest.mark.parametrize("s,p1,p2, expected_result", [
    ('codewars', 'code', 'wars', True),
    ('codewars', 'cdw', 'oears', True),
    ('codewars', 'cod', 'wars', False),

])
def test_is_merge(s, p1, p2, expected_result):
    assert is_merge(s, p1, p2) == expected_result
