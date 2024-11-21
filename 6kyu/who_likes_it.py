# https://www.codewars.com/kata/5266876b8f4bf2da9b000362
def likes(names):
    x = ""
    if len(names) == 0:
        x = "no one likes this"
    elif len(names) == 1:
        x = str(names[0]) + " likes this"
    elif len(names) == 2:
        x = str(names[0]) + " and " + str(names[1]) + " like this"
    elif len(names) == 3:
        x = str(names[0]) + ", " + str(names[1]) + " and " + str(names[2]) + " like this"
    else:
        x = str(names[0]) + ", " + str(names[1]) + " and " + str(len(names) - 2) + " others like this"

    return x
