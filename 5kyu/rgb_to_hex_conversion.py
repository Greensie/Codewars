#https://www.codewars.com/kata/513e08acc600c94f01000001
def rgb(r, g, b):
    if r < 0:
        r = 0
    if r > 255:
        r = 255

    if g < 0:
        g = 0
    if g > 255:
        g = 255

    if b < 0:
        b = 0
    if b > 255:
        b = 255

    r_hex1 = str(int(r / 16))
    r_hex2 = str(r % 16)
    g_hex1 = str(int(g / 16))
    g_hex2 = str(g % 16)
    b_hex_1 = str(int(b / 16))
    b_hex_2 = str(b % 16)
    A = [r_hex1, r_hex2, g_hex1, g_hex2, b_hex_1, b_hex_2]

    for x in range(0, len(A)):
        if A[x] == '10':
            A[x] = 'A'
        elif A[x] == '11':
            A[x] = 'B'
        elif A[x] == '12':
            A[x] = 'C'
        elif A[x] == '13':
            A[x] = 'D'
        elif A[x] == '14':
            A[x] = 'E'
        elif A[x] == '15':
            A[x] = 'F'

    return A[0] + A[1] + A[2] + A[3] + A[4] + A[5]