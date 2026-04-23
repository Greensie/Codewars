# https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3
from pytest import mark

abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"

class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.alphabet = alphabet
        self.key = key

    def encode(self, text):
        new_key = self.match_word_length(text)
        result = ""
        for text_letter, key_letter in zip(text, new_key):
            result += self.shift(text_letter, key_letter, True)
        return result

    def decode(self, text):
        new_key = self.match_word_length(text)
        result = ""
        for text_letter, key_letter in zip(text, new_key):
            result += self.shift(text_letter, key_letter, False)
        return result

    def shift(self, word_letter: str, key_letter: str, encode: bool = True) -> str:
        if word_letter not in self.alphabet:
            return word_letter

        int_word_letter = self.alphabet.index(word_letter)
        int_key_letter = self.alphabet.index(key_letter)
        alphabet_length = len(self.alphabet)

        if encode:
            return self.alphabet[(int_word_letter + int_key_letter) % alphabet_length]
        return self.alphabet[(int_word_letter - int_key_letter) % alphabet_length]

    def match_word_length(self, text):
        new_key = ""
        while len(new_key) < len(text):
            new_key += self.key
        return new_key[:len(text)]




@mark.parametrize("text, expected_encoded", [
    ("waffles", "laxxhsj"),
    ("codewars", "rovwsoiv"),
    ("CODEWARS", "CODEWARS")
])
def test_encode(text, expected_encoded):
    vc = VigenereCipher(key, abc)
    assert vc.encode(text) == expected_encoded

@mark.parametrize("text, expected_decoded", [
    ("rovwsoiv", "codewars"),
    ("laxxhsj", "waffles"),
    ("CODEWARS", "CODEWARS")
])
def test_decode(text, expected_decoded):
    vc = VigenereCipher(key, abc)
    assert vc.decode(text) == expected_decoded

