#https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5
from pytest import mark

local_modifiers = {
    "hundred": 100,
}
outer_modifiers = {
    "thousand": 1000,
    "million": 1000000,
}
base_nums = {"zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90}
def parse_int(string):
    str_divided = string.replace("-", " ").split()
    curr = 0
    total = 0
    for num in str_divided:
        if num in base_nums:
            curr += base_nums[num]
        elif num in local_modifiers:
            curr *= local_modifiers[num]
        elif num in outer_modifiers:
            total += curr * outer_modifiers[num]
            curr = 0
        elif num == "and":
            continue

    total += curr
    return total

@mark.parametrize("string, expected", [
    ("seven hundred eighty-three thousand nine hundred and nineteen",783919),
    ("one",1),
    ("twenty", 20),
    ("two hundred forty-six", 246),
    ("one thousand and one", 1001),
])
def test_parse_int(string, expected):
    assert parse_int(string) == expected
