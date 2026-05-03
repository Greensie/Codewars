# https://www.codewars.com/kata/559f89598c0d6c9b31000125
def archers_ready(archers):
    if len(archers) == 0:
        return False
    return not min(archers) < 5
