# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272
import pytest

alphabet = "abcdefghijklmnopqrstuvwxyz"


def high(x: str) -> str:
    words = x.split()

    def score(word: str) -> int:
        total = 0
        for letter in word:
            total += alphabet.index(letter) + 1
        return total

    return max(words, key=score)


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("man i need a taxi up to ubud", "taxi"),
        ("what time are we climbing up the volcano", "volcano"),
        ("take me to semynak", "semynak"),
        ("d bb", "d"),
    ],
)
def test_high(sentence: str, expected: str):
    assert high(sentence) == expected
