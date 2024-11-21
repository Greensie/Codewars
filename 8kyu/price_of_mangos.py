# https://www.codewars.com/kata/57a77726bb9944d000000b06
def mango(quantity, price):
    discnum = int(quantity / 3)
    price = quantity * price - discnum * price
    return price
