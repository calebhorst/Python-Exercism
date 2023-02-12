def score(x, y):
    x = abs((x**2 + y**2) ** 0.5)
    if x <= 1: return 10
    if x <= 5: return 5
    if x <= 10: return 1
    return 0
