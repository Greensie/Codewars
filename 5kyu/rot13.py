# https://www.codewars.com/kata/530e15517bc88ac656000716
def rot13(message):
    ASCII_values = []
    ret = ''
    for letters in message:
        ASCII_values.append(ord(letters))

    for i in range(0, len(ASCII_values)):
        temp = 0
        if ASCII_values[i] >= 65 and ASCII_values[i] <= 90:
            ASCII_values[i] += 12
            if ASCII_values[i] >= 90:
                temp = ASCII_values[i] - 90
                ASCII_values[i] = 65 + temp
            else:
                ASCII_values[i] += 1
        elif ASCII_values[i] >= 97 and ASCII_values[i] <= 122:
            ASCII_values[i] += 12
            if (ASCII_values[i]) >= 122:
                temp = ASCII_values[i] - 122
                ASCII_values[i] = 97 + temp
            else:
                ASCII_values[i] += 1
        else:
            ASCII_values[i] = ASCII_values[i]

    for letters in ASCII_values:
        ret += chr(letters)

    return ret
