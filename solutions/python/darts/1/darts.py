def score(x, y):

    r = (x**2 + y**2)**(0.5)

    if  0 <= r <= 1:
        return 10
    elif 1 < r <= 5:
        return 5
    elif 5 < r <= 10:
        return 1
    else:
        return 0