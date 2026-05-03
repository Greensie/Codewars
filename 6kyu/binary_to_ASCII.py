def binary_to_string(binary):
    if binary == "":
        return ""

    binary_str = binary
    letters = []
    while binary_str:
        letters.append(binnary_to_ASCII(binary_str[:8]))
        binary_str = binary_str[8:]

    ret_str = ""
    for letter in letters:
        ret_str += letter

    return ret_str


def binnary_to_ASCII(str) -> str:
    listOfNums = list(str)
    i = 0
    num = 0
    n = 7
    while i < 8:
        num += int(listOfNums[i]) * (2**n)
        i += 1
        n -= 1
    return chr(num)


# print(binnary_to_ASCII('01001000'))

bin = "0100100001100101011011000110110001101111"
print(binary_to_string(bin))
