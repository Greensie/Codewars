# https://www.codewars.com/kata/54ff3102c1bad923760001f3
def get_count(sentence):
    count = 0
    for el in sentence:
        if el == "a" or el == "e" or el == "o" or el == "u" or el == "i":
            count += 1
    return count
