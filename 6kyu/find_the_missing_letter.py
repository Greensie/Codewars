#https://www.codewars.com/kata/5839edaa6754d6fec10000a2
def find_missing_letter(chars):
    ASCII_values = []
    for c in chars:
        ASCII_values.append(ord(c))

    for i in range(1, len(ASCII_values)):
        if ASCII_values[i] - ASCII_values[i - 1] != 1:
            x = ASCII_values[i] - 1

    return chr(x)