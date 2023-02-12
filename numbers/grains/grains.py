def square(number):
    if number > 64 or number <= 0:
        raise ValueError("square must be between 1 and 64")
    else:
        grains_on_square = 2 ** (number - 1)
    return grains_on_square


def total():
    sum = 0
    for i in range(1, 64+1) :
        sum = sum + square(i)
    return sum
